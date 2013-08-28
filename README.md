#CairoPlot

CairoPlot is a pure Python plotting library which uses Cairo C/Python API to
create astonishing charts in a easy and intuitive way, perfect fot for
presentations, websites and papers.

It was recognized by the great aesthetics originally conceived by [Rodrigo
Araujo](https://github.com/rodrigoaraujo01).

Official site: [CairoPlot](http://cairoplot.sourceforge.net/index.html)

##Some Plotting Demos

###Functions

    data = [ lambda x : 1, lambda y : y**2, lambda z : -z**2 ]
    colors = ['red', 'orange', 'yellow']
    cairoplot.function_plot( 'function.png', data, 800, 600, grid = True, step = 0.1 )


![Functions Plot Demo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/color_themes_function.png)

###Discrete functions

    data = lambda x: [1,2,3,4,5][x]
    x_labels = ['4', '3', '2', '1', '0']
    cairoplot.function_plot('discrete.png', data, 800, 600,
                            discrete = True, dots = True, grid = True,
                            x_labels = x_labels, x_bounds=(0,4), step = 1)

![Function Plot Demo 2](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/function_3_labels.png)

###Scatter Plot

    data = [(-1, -16, 12), (-12, 17, 11), (-4, 6, 5), (4, -20, 12), (13, -3, 21),
            (7, 14, 20), (-11, -2, 18), (19, 7, 18), (-10, -19, 15), (-17, -2, 6),
            (-9, 4, 10), (14, 11, 16), (13, -11, 18), (20, 20, 16), (7, -8, 15),
            (-16, 17, 16), (16, 9, 9), (-3, -13, 25), (-20, -6, 17), (-10, -10, 12),
            (-7, 17, 25), (10, -10, 13), (10, 13, 20), (17, 6, 15), (18, -11, 14),
            (18, -12, 11), (-9, 11, 14), (17, -15, 25), (-2, -8, 5), (5, 20, 20),
            (18, 20, 23), (-20, -16, 17), (-19, -2, 9), (-11, 19, 18), (17, 16, 12),
            (-5, -20, 15), (-20, -13, 10), (-3, 5, 20), (-1, 13, 17), (-11, -9, 11)]
    colors = [ (0,0,0,0.25), (1,0,0,0.75) ]
    cairoplot.scatter_plot ('scatter.png', data = data, width = 800, height = 600,
                            border = 20, axis = True, discrete = True, dots = 2,
                            grid = True, x_title = 'x axis', y_title = 'y axis',
                            circle_colors = colors )

![Scatter Plot Demo 2](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/scatter_4_variable_radius.png)

###Error bars

    t = [x*0.1 for x in range(0,40)]
    f = [math.exp(x) for x in t]
    g = [10*math.cos(x) for x in t]
    h = [10*math.sin(x) for x in t]
    erx = [0.1*random.random() for x in t]
    ery = [5*random.random() for x in t]
    data = {'exp' : [t,f], 'cos' : [t,g], 'sin' : [t,h]}
    series_colors = [ (1,0,0), (0,0,0), (0,0,1) ]
    cairoplot.scatter_plot ('error_bars.png', data = data,
                            errorx = [erx,erx], errory = [ery,ery],
                            width = 800, height = 600, border = 20,
                            axis = True, discrete = False, dots = 5, grid = True,
                            x_title = 't', y_title = 'f(t) g(t)',
                            series_legend=True, series_colors = series_colors)

![Scatter Plot Demo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/color_themes_scatter.png)

###Donut Plot

    background = cairo.LinearGradient(300, 0, 300, 400)
    background.add_color_stop_rgb(0,0.4,0.4,0.4)
    background.add_color_stop_rgb(1.0,0.1,0.1,0.1)
    data = {'john' : 700, 'mary' : 100, 'philip' : 100 , 'suzy' : 50, 'yman' : 50}
    cairoplot.donut_plot('donut.png', data, 800, 600, background = background,
                         gradient = True, shadow = True, inner_radius = 0.3)

![Donut PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/donut_3_background.png)

###Pie Plot

    background = cairo.LinearGradient(300, 0, 300, 400)
    background.add_color_stop_rgb(0.0,0.7,0.0,0.0)
    background.add_color_stop_rgb(1.0,0.3,0.0,0.0)
    data = {'orcs' : 100, 'goblins' : 230, 'elves' : 50 , 'demons' : 43,
            'humans' : 332}
    cairoplot.pie_plot('pie.png', data, 800, 600, background = background,
                       gradient = True, shadow = True)

![Pie PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/pie_3_background.png)

###Gantt Chart

    pieces = [(0.5, 5.5), [(0, 4), (6, 8)], (5.5, 7), (7, 9)]
    x_labels = ['teste01', 'teste02', 'teste03', 'teste04']
    y_labels = ['0001', '0002', '0003', '0004', '0005',
                '0006', '0007', '0008', '0009', '0010']
    colors = [(1.0, 0.0, 0.0), (1.0, 0.7, 0.0), (1.0, 1.0, 0.0), (0.0, 1.0, 0.0)]
    cairoplot.gantt_chart('gantt.png', pieces, 800, 600, x_labels, y_labels, colors)

![Gantt PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/gantt_1_default.png)

###Horizontal Bars

    data = [27, 10, 18, 5, 1, 22]
    cairoplot.horizontal_bar_plot('horizontal.png', data, 800, 600, border = 20,
                                  display_values = True, grid = True, rounded_corners = True)

![Horizontal Bar PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/hbar_0_dictionary.png)

###Horizontal Bars Stacked

    data = [[6, 4, 10], [8, 9, 3], [1, 10, 9], [2, 7, 11]]
    colors = [(1,0.2,0), (1,0.7,0), (1,1,0)]
    y_labels = ['teste1', 'teste2', 'testegrande3', 'testegrande4']
    cairoplot.horizontal_bar_plot('stack.png', data, 800, 600, border = 20,
                                  display_values = True, grid = True, rounded_corners = True,
                                  stack = True, y_labels = y_labels, colors = colors)

![Horizontal Stack Bar PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/hbar_10_stack.png)

###Vertical Bars

    data = [[0, 3, 11], [8, 9, 21], [13, 10, 9], [2, 30, 8]]
    colors = [(1,0.2,0), (1,0.7,0), (1,1,0)]
    series_labels = ['red', 'orange', 'yellow']
    cairoplot.vertical_bar_plot('vertical.png', data, 800, 600, border = 20,
                                series_labels = series_labels, display_values = True, grid = True,
                                rounded_corners = True, colors = colors)

![Vertical Bar PlotDemo](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/vbar_2_rounded.png)

###Vertical Bars Grouped

    data = [[3,4], [4,8], [5,3], [9,1]]
    y_labels = ['line1', 'line2', 'line3', 'line4', 'line5', 'line6']
    x_labels = ['group1', 'group2', 'group3', 'group4']
    cairoplot.vertical_bar_plot('groups.png', data, 800, 600, border = 20,
                                display_values = True, grid = True,
                                x_labels = x_labels, y_labels = y_labels )

![Vertical Bar Plot Demo 2](https://github.com/magnunleno/cairoplot/raw/develop/demo-graphs/vbar_8_hy_labels.png)


##Some Legal Stuff


The MIT License (MIT)

Copyright (c) 2013 Cairoplot team

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
