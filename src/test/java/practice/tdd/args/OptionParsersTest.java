package practice.tdd.args;

import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import practice.tdd.args.exceptions.IllegalValueException;
import practice.tdd.args.exceptions.InsufficientArgumentsException;
import practice.tdd.args.exceptions.TooManyArgumentsException;

import java.lang.annotation.Annotation;
import java.util.List;
import java.util.function.Function;

import static java.util.Arrays.asList;
import static org.junit.jupiter.api.Assertions.*;

public class OptionParsersTest {
    @Nested
    class UnaryOptionParserTest {
        @Test
        public void should_not_accept_extra_argument_for_single_valued_option() {
            TooManyArgumentsException e = assertThrows(
                    TooManyArgumentsException.class,
                    () -> OptionParsers.unary(0, Integer::parseInt)
                            .parse(asList("-p", "8080", "8081"), option("p"))
            );
            assertEquals("p", e.getOption());
        }

        @ParameterizedTest
        @ValueSource(strings = {"-p -l", "-p"})
        public void should_not_accept_insufficient_argument_for_single_valued_option(String arguments) {
            InsufficientArgumentsException e = assertThrows(
                    InsufficientArgumentsException.class,
                    () -> OptionParsers.unary(0, Integer::parseInt)
                            .parse(asList(arguments.split(" ")), option("p"))
            );
            assertEquals("p", e.getOption());
        }

        @Test
        public void should_not_accept_extra_argument_for_string_single_valued_option() {
            TooManyArgumentsException e = assertThrows(
                    TooManyArgumentsException.class,
                    () -> OptionParsers.unary("", String::valueOf)
                            .parse(asList("-d", "/foo", "/bar"), option("d"))
            );
            assertEquals("d", e.getOption());
        }

        @ParameterizedTest
        @ValueSource(strings = {"-d -l", "-d"})
        public void should_not_accept_insufficient_argument_for_string_single_valued_option(String arguments) {
            InsufficientArgumentsException e = assertThrows(
                    InsufficientArgumentsException.class,
                    () -> OptionParsers.unary("", String::valueOf)
                            .parse(asList(arguments.split(" ")), option("d"))
            );
            assertEquals("d", e.getOption());
        }

        @Test
        public void should_set_default_value_if_option_not_present() throws TooManyArgumentsException {
            Function<String, Object> whatEver = (it) -> null;
            Object default_value = new Object();

            assertSame(default_value, OptionParsers.unary(default_value, whatEver)
                    .parse(List.of(), option("p")));
        }

        @Test
        public void should_parse_int_as_option_value() {
            assertEquals(8080, OptionParsers.unary(0, Integer::parseInt).parse(List.of("-p", "8080"), option("p")));
        }

        // -d /some/path
        @Test
        public void should_parse_string_as_option_value() {
            assertEquals("/foo/bar", OptionParsers.unary("", String::valueOf).parse(List.of("-d", "/foo/bar"), option("d")));
        }

        @Test
        public void should_parse_value_if_flag_presents() {
            Object parsed = new Object();
            Function<String, Object> parse = (it) -> parsed;
            Object what_ever = new Object();
            assertSame(parsed, OptionParsers.unary(what_ever, parse).parse(List.of("-x", "sss"), option("x")));
        }
    }

    @Nested
    class BooleanOptionsParserTest {
        @Test
        public void should_set_boolean_option_to_true_if_flag_presents() {
            assertTrue(OptionParsers.bool().parse(List.of("-l"), option("l")));
        }

        @Test
        public void should_not_accept_extra_arguments_for_boolean_option() {
            TooManyArgumentsException e = assertThrows(TooManyArgumentsException.class, () -> OptionParsers.bool().parse(asList("-l", "t"), option("l")));
            assertEquals("l", e.getOption());
        }

        @Test
        public void should_set_default_value_to_false_if_option_not_present() throws TooManyArgumentsException {
            assertFalse(OptionParsers.bool().parse(List.of(), option("a")));
        }
    }

    @Nested
    class ListOptionParserTest {
        @Test
        public void should_parse_list_of_values() {
            assertArrayEquals(new String[]{"this", "is"}, OptionParsers.list(String[]::new, String::valueOf).parse(List.of("-g", "this", "is"), option("g")));
        }

        @Test
        public void should_not_treat_negative_int_as_flag() {
            assertArrayEquals(new Integer[]{-1, -2}, OptionParsers.list(Integer[]::new, Integer::parseInt).parse(List.of("-g", "-1", "-2"), option("g")));
        }

        @Test
        public void should_use_empty_array_as_default_value() {
            assertArrayEquals(new String[]{}, OptionParsers.list(String[]::new, String::valueOf).parse(List.of(), option("g")));
        }

        @Test
        public void should_throw_exception_if_value_parser_cant_parse_value() throws TooManyArgumentsException {
            Function<String, String> parser = (it) -> {
                throw new RuntimeException();
            };
            IllegalValueException e = assertThrows(IllegalValueException.class, () -> OptionParsers.list(String[]::new, parser).parse(List.of("-g", "this", "is"), option("g")));
            assertEquals("g", e.getOption());
            assertEquals("this", e.getValue());
        }
    }

    static Option option(String value) {
        return new Option() {
            @Override
            public Class<? extends Annotation> annotationType() {
                return Option.class;
            }

            @Override
            public String value() {
                return value;
            }
        };
    }
}
