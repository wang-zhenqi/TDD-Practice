# TDD 练习

这个代码库保存了关于“测试驱动开发（Test Driving Development, TDD）” 的练习代码，素材来自于“极客时间”上的课程：“[徐昊 · TDD 项目实战 70 讲](https://time.geekbang.org/column/intro/100109401?tab=catalog)”。

练习方法是：观看老师的演示视频，按照其步骤重新思考、内化之后，自己用同样的方式以 Python 代码实现相同的功能。在练习的过程中我会不断记录代码的演进过程以及思考过程。

## 实战项目一 命令行参数解析

具体的分析以及实现过程见[命令行参数解析 - 任务分析](cmd_arg_parser/doc/RequirementAnalysis.md)

### 操作记录

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
    options = Options()</br>arg_mapping = {
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
            option_parser = ParserFactory().get_parser_by_option_type(
                option_type=typing.get_type_hints(Options).get(option_fields_map[arg])
            )

        setattr(options, option_fields_map[arg], option_parser.parse(index, arguments_list))
    return options
```

</td>
</tr>
</table>

可以看到，函数中嵌套定义的函数会让代码看起来很不美观。另外前者的 `parse_value` 方法也缺乏灵活性。关于灵活性，在目前的代码中，也许还不是大问题，也不需要过度设计，但是在未来程序变复杂后，这里迟早是要改掉的。
