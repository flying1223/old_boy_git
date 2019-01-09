'''

'''
'''
HTML
    1.一套浏览器认识的规则
    2.开发者：
        学习html规则
        开发后台程序
            写HTML文件（充当模板）
            数据库获取数据，然后替换到HTML文件的指定位置（web 框架）
    3.本地测试
        找到文件路径，浏览器打开
        pycharm打开
    4.编写HTML文件
        doctype对应关系 
        HTML标签，标签内部可以写属性  只能有一个HTML标签
        注释 <!--  注释的内容  -->
    5.标签分类
        自闭合标签   <meta charset="UTF-8">
        主动闭合标签  <title>百度</title>
    6.head标签
        <meta> 编码，跳转，刷新，关键字，描述，兼容
        title标签
        <link/> 图标
        <style/>
        <script/>
    7.body标签
        -图标：&nbsp;  &gt;  &lt;
        -p标签     段落
        -br标签    换行
        -----小总结-----
            所以标签分为：
                快级标签：    h系列（特点：加大加粗），p系列（段落和段落之间有间距） div(白板)
                行内标签：    span标签（白板，不带任何特性）
            标签之间可以嵌套
            标签存在的意义：定位操作，css操作，js操作
            Chrome：审查元素的使用
                ——定位
                ——查看样式
        -input系列——s6+form标签
            input type='text'       -name属性 value='故宫'
            input type='password'   -name属性
            input type='button'     -value='提交' 按钮
            input type='submit'     -value='登录' 提交按钮，表单form标签
            input type='reset'      -重置，清空选项
            input type='radio'      -单选框 value，checked="checked"默认值，name（name相同）互斥
            input type='checkBox'   -复选框 value，checked="checked"默认值，name（批量操作）
            input type='file'       -依赖form表单的一个属性 enctype="multipart/form-data"
            <textarea>默认值</textarea>    -name属性 多行文本输入
            select标签               -name，内部option value，提交到后台，size，muiltiple（多选）
        -a标签——s7
            - 跳转
            - 锚 herf="#某个标签的id" 标签id不允许重复
        -img——s8
            - src
            - alt
            - title
        -列表——s8
            -ul     li
            -ol     li
            -dl     dt  dd
        -表格——s9
            table
                thead
                    tr  
                        th
                tbody
                    tr
                        td
            colspan     列合并
            rowspan     行和并
        -label——s10
            用于点击文字，使得关联的标签获取光标
        -fieldset——s10
            legend
                   
    -20个标签
    
CSS
    在标签上设置style属性
        background-color:#ff5722;
        height:48px
        。。。
    编写css样式——s11
        1.标签的style属性
        2.写在head里面  style标签中写样式
            -id选择区
                #i1{
                    background-color:#ff5722;
                    height:48px
                }
            -class选择器
                    .c1{
                        ...
                    }
                    <div class="c1">4</div>
            -标签选择器
                    div{
                        background-color:black;
                        color:white;
                    }
                    所有div设置上此样式
            -层级选择器（空格）
                    .c1 .c2 div{
                    ...
                    }
            -组合选择器（逗号）
                    .c2,.c3,.c4,#c5{
                    ...
                    }
            -属性选择器
                    input[type='text']{width:100px;height:200px}
                    input[n='fff']{width:100px;height:200px}
                    .c777[n='flying']{width:10px;height:20px} 
        2.5 css样式也可以写在单独的文件中
                    <link rel="stylesheet" href="css/commons.css">

            ps:
                优先级，标签上style优先，编写顺然，就近原则（靠下的优先）                                   
        3.注释
            /*      */
        4.边框--s14
            -宽度，样式，颜色（border:4px dotted red;）
            -border-left
        5.--s14
            height,         高度
            width,          宽度 （像素 百分比）
            text-align: center  水平方向居中
            line-height,    垂直方向根据标签高度
            color,          字体颜色
            font-size,      字体大小
            font-weight     字体加粗
        6.float--s15
            让标签浪起来，块级标签也可以堆叠
            父级管不住
                <div style="clear:both;"></div>
        7.display--s17
            display: none;  让标签消失
            display: inline;
            display: block;
            display: inline-block;
                        具有inline，默认自己有多少占多少
                        具有block，可以设置高度，宽度，边距 （padding margin）
            ***
            行内标签：无法设置高度，宽度，边距 （padding margin）
            块级标签：可以设置高度，宽度，边距 （padding margin）
        8.padding margin（0 auto）
            边距，
            padding 内边距

            margin  外边距
    
    -颜色
    -位置
'''

