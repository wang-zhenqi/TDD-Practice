# 命令行参数解析 - 任务分析

## 需求描述

> 我们中的大多数人都不得不时不时地解析一下命令行参数。如果我们没有一个方便的工具，那么我们就简单地处理一下传入 main 函数的字符串数组。有很多开源工具可以完成这个任务，但它们可能并不能完全满足我们的要求。所以我们再写一个吧。
>
> 传递给程序的参数由标志和值组成。标志应该是一个字符，前面有一个减号。每个标志都应该有零个或多个与之相关的值。例如：
>
> `-l -p 8080 -d /usr/logs`
>
> - “l”（日志）没有相关的值，它是一个布尔标志，如果存在则为 true，不存在则为 false。
>
> - “p”（端口）有一个整数值。
>
> - “d”（目录）有一个字符串值。
>
> 标志后面如果存在多个值，则该标志表示一个列表：
>
> `-g this is a list -d 1 2 -3 5`
>
> - "g"表示一个字符串列表[“this”, “is”, “a”, “list”]。
>
> - “d"标志表示一个整数列表[1, 2, -3, 5]。
>
> 如果参数中没有指定某个标志，那么解析器应该指定一个默认值。例如，false 代表布尔值，0 代表数字，”"代表字符串，[]代表列表。如果给出的参数与模式不匹配，重要的是给出一个好的错误信息，准确地解释什么是错误的。
>
> 确保你的代码是可扩展的，即如何增加新的数值类型是直接和明显的。

## 任务拆解

### 1. 大致构思软件被使用的方式，把握对外接口的方向

从需求描述中可以看出，该需求要求实现一个命令行程序，接收若干参数（或者叫选项，options，下文中这两个术语是可互换的）。

我们的命令行程序名称设置为“my_app”，因此可以以如下方式使用：

1. `my_app -l -p 8080 -d /some/path`. 解析后得到的数据分别为：`logging: True`，`port: 8080`，`directory: /some/path`.
2. `my_app -g this is a list -d 1 2 -3 5`. 解析后得到的数据分别为：`group: ["this", "is", "a", "list"]`，`digit: [1, 2, -3, 5]`.

### 2. 大致构思功能的实现方式，划分所需的组件（Component）以及组件间的关系（所谓的架构）

这一步如果暂时还没有思路可以省略。

到目前来看我们大概知道需要对参数依据空格进行拆分，对拆分后的部分按照规则再进行分析。

### 3. 根据需求的功能描述拆分功能点，功能点要考虑正确路径（Happy Path）和边界条件（Sad Path）

这一步非常重要，是否能正确拆分功能点，决定了要写哪些测试样例。

#### Happy Path

- omitted argument
    - `my_app`
- single argument with single values
    - `my_app -l`
    - `my_app -p 8080`
    - `my_app -d /some/path`
- multiple single-valued arguments
    - `my_app -l -p 8080 -d /some/path`
- single list-valued argument
    - `my_app -g this is a list`
    - `my_app -d 1 2 -3 5`
- multiple list-valued arguments
    - `my_app -g this is a list -d 1 2 -3 5`
- put them all together
    - `my_app -l -p 8080 -d /some/path -g this is a list -d 1 2 -3 5`

#### Sad Path

- `my_app -l 1`: -l 选项不带数值
- `my_app -p`: -p 选项需要数值
- `my_app -p abcd`: -p 选项需要整型数值
- `my_app -d 10 abc true`: -d 选项在有多个数值时，要求每个数值均为整型

在边界条件中，需要给出提示，指明为什么参数与模式不匹配。

#### 默认值

- boolean: false
- integer: 0
- string: ""
- list: []

### 4. 依照组件以及组件间的关系，将功能拆分到对应组件

暂略

### 5. 针对拆分的结果编写测试，进入红 / 绿 / 重构循环

具体代码见 "test/" 和 "src/"
