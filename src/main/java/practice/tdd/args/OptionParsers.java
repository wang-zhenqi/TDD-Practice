package practice.tdd.args;

import practice.tdd.args.exceptions.IllegalValueException;
import practice.tdd.args.exceptions.InsufficientArgumentsException;
import practice.tdd.args.exceptions.TooManyArgumentsException;

import java.util.List;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.IntFunction;
import java.util.stream.IntStream;

class OptionParsers {
    public static OptionParser<Boolean> bool() {
        return (arguments, option) -> getPossibleArgumentList(arguments, option, 0).isPresent();
    }

    public static <T> OptionParser<T> unary(T default_value, Function<String, T> process_function) {
        return (arguments, option) -> getPossibleArgumentList(arguments, option, 1).map(it -> parseValue(option, it.get(0), process_function)).orElse(default_value);
    }

    public static <T> OptionParser<T[]> list(IntFunction<T[]> generator, Function<String, T> process_function) {
        return (arguments, option) -> getPossibleArgumentList(arguments, option)
                .map(
                        it -> it.stream().map(
                                value -> parseValue(option, value, process_function)
                        ).toArray(generator)
                ).orElse(generator.apply(0));
    }

    private static <T> T parseValue(Option option, String value, Function<String, T> process_function) {
        try {
            return process_function.apply(value);
        } catch (Exception e) {
            throw new IllegalValueException(option.value(), value);
        }
    }

    private static Optional<List<String>> getPossibleArgumentList(List<String> arguments, Option option, int expectedSize) {
        return getPossibleArgumentList(arguments, option).map(it -> checkSize(option, expectedSize, it));
    }

    private static List<String> checkSize(Option option, int expectedSize, List<String> next_values) {
        if (next_values.size() < expectedSize) {
            throw new InsufficientArgumentsException(option.value());
        }
        if (next_values.size() > expectedSize) {
            throw new TooManyArgumentsException(option.value());
        }
        return next_values;
    }

    private static Optional<List<String>> getPossibleArgumentList(List<String> arguments, Option option) {
        int index = arguments.indexOf("-" + option.value());
        return Optional.ofNullable(index == -1 ? null : getNextValues(arguments, index));
    }

    private static List<String> getNextValues(List<String> arguments, int index) {
        return arguments.subList(index + 1, IntStream.range(index + 1, arguments.size())
                .filter(it -> arguments.get(it).matches("^-[a-zA-Z-]+$"))
                .findFirst().orElse(arguments.size()));
    }
}
