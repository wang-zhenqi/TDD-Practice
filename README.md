# TDD 练习

这个代码库保存了关于“测试驱动开发（Test Driving Development, TDD）” 的练习代码，素材来自于“极客时间”上的课程：“[徐昊 · TDD 项目实战 70 讲](https://time.geekbang.org/column/intro/100109401?tab=catalog)”。

练习方法是：观看老师的演示视频，按照其步骤重新思考、内化之后，自己用同样的方式以 Python 代码实现相同的功能。在练习的过程中我会不断记录代码的演进过程以及思考过程。

## 实战项目一 命令行参数解析

具体的分析以及实现过程见[命令行参数解析 - 任务分析](cmd_arg_parser/doc/RequirementAnalysis.md)

### 实现单参数选项的 Happy Path

在完成 Happy Path 的过程中，有以下几个值得记录的转折点：
1. 将 arguments 作为字符串来处理
2. 将 arguments 改为参数列表
3. 引入 Pydantic 来定义各选项
4. 使用 Lambda 函数来处理参数值
5. 引入 OptionParser 类及其工厂类来选择处理参数值的方式

最初，我使用了字符串来作为选项的输入，用 `str.split()` 方法来分割各选项。这种方式的好处在于对于一个类似 `-l -d /some/path -p 8080` 这样的字符串，我可以很容易地将它分割成“选项-参数”字符串列表：`["-l", "-d /some/path", "-p 8080"]`，然后再对每一个元素进行处理。这种处理方式较为方便，天然地具备乱序处理的能力。

后来由于 Python 程序会自动将这些参数作为列表（`sys.argv`）传入：`["-l", "-d", "/some/path", "-p", "8080"]`，那么上面的字符串处理就有些不适用了，因此我改成了处理参数列表。

之后就是对选项的定义，最初只是用了一个列表的形式存放参数值：`[False, 0, "", [], []]`，但这种方式一来可读性差，二来列表中的元素很难与实际参数对应，只能通过位置来选择元素，并且缺少对选项数据类型的约束。因此引入 Pydantic 来定义选项是一个较为便捷的方式，这里其实也可自己定义一个类结构，但既然已有 Pydantic，那么倒也没太大必要自己手写一个功能类似的类了。

使用 Lambda 函数来对参数值进行处理可以让代码简短一些，但缺点是可读性略差，在某一函数的参数中传入 Lambda 结构，会破坏代码表意的连续性。因此在后来的重构中把它去除了。

经过以上步骤，得到了一个逻辑简单，但是冗长的 `process_arg_list` 方法。因此想要对这个函数再进行一些精简。这些都是用自己的思路一步步完成到这里，发现还是使用课程中的**抽象类**和**工厂类**单独生成 parser 会让代码更易理解。于是在最后一步，同样采用了这个方法。可以对比一下前后的差距：

<table>
<tr>
<td>Before</td>
<td>After</td>
</tr>
<tr>
<td>

```python
def process_arg_list(arguments: List[str]):
    options = Options()
    
    arg_mapping = {
        "-l": "logging",
        "-p": "port",
        "-d": "directory",
    }
    
    for index, arg in enumerate(iter(arguments)):
        def parse_value(arg_type):
            if arg_type == bool:
                return True
            return arg_type(arguments[index + 1])
        
        def get_field_type():
            return typing.get_type_hints(Options).get(arg_mapping[arg])
            
        if arg in arg_mapping:
            setattr(options, arg_mapping[arg], parse_value(get_field_type()))
    return options
```

</td>
<td>

```python
def process_arguments(arguments_list: List[str]):
    options = Options()
    for index, arg in enumerate(iter(arguments_list)):
        if arg in option_fields_map:
            option_parser = get_parser_by_option_type(
                option_type=typing.get_type_hints(Options).get(option_fields_map[arg])
            )

        setattr(options, option_fields_map[arg], option_parser.parse(arguments_list, index))
    return options
```

</td>
</tr>
</table>

可以看到，函数中嵌套定义的函数会让代码看起来很不美观。另外前者的 `parse_value` 方法也缺乏灵活性。关于灵活性，在目前的代码中，也许还不是大问题，也不需要过度设计，但是在未来程序变复杂后，这里迟早是要改掉的。

### 实现单参数选项的 Sad Path

这里的实现比较简单，主要就是新增了一些 Exception 的定义。后将 Parser 重构了一下，由工厂类接收选项的类型，生成不同的 parser。

### 重新安排测试用例

在开始多参数选项的开发前，由于我们新增了各种 Parser，因此可以将原本面向整个实现（my_app.process_arguments()）的测试转移到更为细化的不同 parser.parse() 中去。测试范围更小会使得代码更加可控，更容易定位问题。

### 再次进行神奇的重构

这里再次重构的原因是因为发现代码中仍然有一些不易察觉的坏味道：在 SingleValuedOptionParser 类中，两条检查参数数量的语句看起来很不直观：

```python
if len(argument_list) - index > 2 and not argument_list[index + 2].startswith("-"):
    raise TooManyArgumentsException(argument_list[index])
if (len(argument_list) - index > 1 and argument_list[index + 1].startswith("-")) or \
        len(argument_list) - index == 1:
    raise NotSufficientArgumentException(argument_list[index])
```

对读者来说，一下看到如此复杂的条件语句是很不容易搞清楚它的内在逻辑的。因此最简单的方式是“加注释”，解释一下这两个条条件语句的判断逻辑。然而随意添加注释本就是坏味道的一种，代码应该是表意的，而非需要注释才能让人读懂。（只有在逻辑无法用代码描述的情况下，例如应用了某种数学公式，无法用代码说明，才应使用说明性的注释。）

因此，这里我们首先选择将条件语句抽取成函数：`too_many_arguments()` 和 `insufficient_arguments()`。这样代码的可读性就大大增强了。

接下来我们仔细观察 `BooleanOptionParser` 和 `SingleValuedOptionParser` 就可以发现，它们的 `parse()` 方法的操作逻辑其实是一样的：都是先判断参数的数量，决定是否要抛出异常，然后再对参数进行处理。那么我们其实就可以引入一个通用的方法来检查参数，以简化代码逻辑：

```python
def validate_the_quantity_of_applicable_arguments(argument_list,
                                                  index,
                                                  max_number_of_arguments,
                                                  min_number_of_arguments):
    applicable_arguments_list = get_applicable_argument_list(argument_list, index)
    if too_many_arguments(applicable_arguments_list, max_number_of_arguments):
        raise TooManyArgumentsException(argument_list[index])
    if insufficient_arguments(applicable_arguments_list, min_number_of_arguments):
        raise InsufficientArgumentException(argument_list[index])
    return applicable_arguments_list
```

再将它们的全部逻辑转移到基类 `OptionParser` 中去，这样这两个子类就可以废弃了：

```python
def parse(self, argument_list, index):
    applicable_arguments_list = validate_the_quantity_of_applicable_arguments(
        argument_list,
        index,
        self.max_number_of_arguments,
        self.min_number_of_arguments)

    try:
        result = self.parsing_function(applicable_arguments_list[0])
    except ValueError as e:
        raise ValueError(f"The type of argument: {applicable_arguments_list[0]} is invalid.\nDetail: {str(e)}")
    else:
        return result
```

相应地修改测试用例中的代码，最终就得到了一个非常清晰且精简的代码。

由此我们可以看到，关于解析 boolean，int，和 str 类型的参数，我们由最初的写在一起，到分别创建 Parser 类，再到最终又合并到了一起，背后完成了大量的重构，代码的逻辑在不断完善，这就是 TDD 的厉害之处，每次只专注于一个目标，小步快跑，不断优化。如果从最开始就想设计一个如现在版本一样的代码结构，那要多花很多时间。而且，在花费这些时间的过程中，我们的思维方式仍然是模拟——试错——改进的过程，本质上并没有比 TDD 更加高明。