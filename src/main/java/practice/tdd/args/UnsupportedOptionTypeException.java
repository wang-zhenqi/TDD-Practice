package practice.tdd.args;

public class UnsupportedOptionTypeException extends RuntimeException {
    String option;
    Class<?> type;
    public UnsupportedOptionTypeException(String option, Class<?> type) {
        this.option = option;
        this.type = type;
    }


    public String getOption() {
        return this.option;
    }

    public Class<?> getType() {
        return this.type;
    }
}
