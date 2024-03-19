package practice.tdd.args;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import practice.tdd.args.exceptions.IllegalOptionException;

import static org.junit.jupiter.api.Assertions.*;

public class ArgsTest {
    // -l -p 8080 -d /some/path
    @Test
    public void should_example_1() {
        Options options = Args.parse(Options.class, "-l", "-p", "8080", "-d", "/some/path");
        assertTrue(options.logging());
        assertEquals(8080, options.port());
        assertEquals("/some/path", options.directory());
    }

    @Test
    public void should_throw_illegal_option_exception_if_annotation_not_present() {
        IllegalOptionException e = assertThrows(IllegalOptionException.class, () -> Args.parse(OptionsWithoutAnnotation.class, "-l", "-p", "8080", "-d", "/some/path"));
        assertEquals("port", e.getParameter());
    }

    record OptionsWithoutAnnotation(@Option("l") boolean logging, int port, @Option("d") String directory) {
    }

    @Test
    public void should_raise_exception_if_type_not_supported() {
        UnsupportedOptionTypeException e = assertThrows(UnsupportedOptionTypeException.class, () -> Args.parse(OptionsWithUnsupportedType.class, "-l", "abc"));
        assertEquals("l", e.getOption());
        assertEquals(Object.class, e.getType());
    }

    record OptionsWithUnsupportedType(@Option("l") Object logging) {
    }

    // -g This is a list -d 1 2 -3 4
    @Test
    public void should_example_2() {
        ListOptions options = Args.parse(ListOptions.class, "-g", "This", "is", "a", "list", "-d", "1", "2", "-3", "4");
        assertArrayEquals(new String[]{"This", "is", "a", "list"}, options.group());
        assertArrayEquals(new Integer[]{1, 2, -3, 4}, options.decimals());
    }

    record Options(@Option("l") boolean logging, @Option("p") int port, @Option("d") String directory) {
    }

    record ListOptions(@Option("g") String[] group, @Option("d") Integer[] decimals) {

    }
}
