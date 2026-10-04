| F-String Format  | Example Value  | Output                 | Meaning / Description                         |
| ---------------- | -------------- | ---------------------- | --------------------------------------------- |
| `{x}`            | `x=42`         | `42`                   | Default formatting                            |
| `{x:s}`          | `x="Bedar"`      | `Bedar`                  | String format                                 |
| `{x:10}`         | `x="Bedar"`      | `Bedar       `           | Width 10, left aligned by default for strings |
| `{x:<10}`        | `x="Bedar"`      | `Bedar       `           | Left align in width 10                        |
| `{x:>10}`        | `x="Bedar"`      | `       Bedar`           | Right align in width 10                       |
| `{x:^10}`        | `x="Bedar"`      | `   Bedar    `           | Center align in width 10                      |
| `{x:*<10}`       | `x="Bedar"`      | `Bedar*******`           | Left align, fill with `*`                     |
| `{x:*>10}`       | `x="Bedar"`      | `*******Bedar`           | Right align, fill with `*`                    |
| `{x:*^10}`       | `x="Bedar"`      | `***Bedar****`           | Center align, fill with `*`                   |
| `{x:.3}`         | `x="Python"`   | `Pyt`                  | Maximum 3 characters                          |
| `{x:d}`          | `x=42`         | `42`                   | Decimal integer                               |
| `{x:5d}`         | `x=42`         | `   42`                | Width 5 integer                               |
| `{x:03d}`        | `x=7`          | `007`                  | Width 3, zero padded                          |
| `{x:05d}`        | `x=42`         | `00042`                | Width 5, zero padded                          |
| `{x:+d}`         | `x=42`         | `+42`                  | Always show sign                              |
| `{x:+d}`         | `x=-42`        | `-42`                  | Always show sign                              |
| `{x: d}`         | `x=42`         | ` 42`                  | Space for positive sign                       |
| `{x:,d}`         | `x=1234567`    | `1,234,567`            | Comma thousands separator                     |
| `{x:_d}`         | `x=1234567`    | `1_234_567`            | Underscore thousands separator                |
| `{x:b}`          | `x=10`         | `1010`                 | Binary (base 2)                               |
| `{x:#b}`         | `x=10`         | `0b1010`               | Binary with prefix                            |
| `{x:o}`          | `x=10`         | `12`                   | Octal (base 8)                                |
| `{x:#o}`         | `x=10`         | `0o12`                 | Octal with prefix                             |
| `{x:x}`          | `x=255`        | `ff`                   | Hexadecimal lowercase                         |
| `{x:X}`          | `x=255`        | `FF`                   | Hexadecimal uppercase                         |
| `{x:#x}`         | `x=255`        | `0xff`                 | Hexadecimal with prefix                       |
| `{x:f}`          | `x=3.14159`    | `3.141590`             | Fixed-point float (6 decimals default)        |
| `{x:.2f}`        | `x=3.14159`    | `3.14`                 | 2 decimal places                              |
| `{x:.4f}`        | `x=3.14159`    | `3.1416`               | 4 decimal places                              |
| `{x:10.2f}`      | `x=3.14159`    | `      3.14`           | Width 10, 2 decimals                          |
| `{x:+.2f}`       | `x=3.14`       | `+3.14`                | Float with sign                               |
| `{x:e}`          | `x=1234`       | `1.234000e+03`         | Scientific notation = 1.234 × 10³             |
| `{x:.2e}`        | `x=1234`       | `1.23e+03`             | Scientific notation, 2 decimals               |
| `{x:E}`          | `x=1234`       | `1.234000E+03`         | Scientific notation uppercase                 |
| `{x:.2E}`        | `x=1234`       | `1.23E+03`             | Scientific notation uppercase, 2 decimals     |
| `{x:g}`          | `x=1234.567`   | `1234.57`              | General format, chooses best representation   |
| `{x:g}`          | `x=0.00001234` | `1.234e-05`            | Automatically switches to scientific notation |
| `{x:.3g}`        | `x=1234.567`   | `1.23e+03`             | 3 significant digits                          |
| `{x:.5g}`        | `x=1234.567`   | `1234.6`               | 5 significant digits                          |
| `{x:%}`          | `x=0.25`       | `25.000000%`           | Percentage × 100                              |
| `{x:.1%}`        | `x=0.857`      | `85.7%`                | Percentage with 1 decimal                     |
| `{x:.2%}`        | `x=0.857`      | `85.70%`               | Percentage with 2 decimals                    |
| `{x=}`           | `x=42`         | `x=42`                 | Debug variable name + value                   |
| `{name=}`        | `name="Bedar"`   | `name='Bedar'`           | Debug output                                  |
| `{x!s}`          | `x=42`         | `42`                   | Convert using `str()`                         |
| `{x!r}`          | `x="Bedar"`      | `'Bedar'`                | Convert using `repr()`                        |
| `{x!a}`          | `x="Bedar"`      | `'Bedar'`                | Convert using `ascii()`                       |
| `{now:%Y}`       | Date           | `2026`                 | Year                                          |
| `{now:%m}`       | Date           | `06`                   | Month                                         |
| `{now:%d}`       | Date           | `25`                   | Day                                           |
| `{now:%H}`       | Date           | `14`                   | Hour (24-hour)                                |
| `{now:%M}`       | Date           | `30`                   | Minute                                        |
| `{now:%S}`       | Date           | `45`                   | Second                                        |
| `{now:%Y-%m-%d}` | Date           | `2026-06-25`           | ISO date                                      |
| `{now:%H:%M:%S}` | Date           | `14:30:45`             | Time                                          |
| `{"="*10}`       | N/A            | `==========`           | Repeat string 10 times                        |
| `{"=-"*5}`       | N/A            | `=-=-=-=-=-`           | Repeat pattern 5 times                        |
| `{"Title":^20}`  | `"Title"`      | `       Title        ` | Center title in width 20                      |
| `{"Title":*^20}` | `"Title"`      | `*******Title********` | Center with decorative fill                   |
