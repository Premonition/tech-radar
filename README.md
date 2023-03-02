## Dependencies
Requires at least python 3.10

## Adding to the chart
Look in `build/input.yml`.
It's split into four sections. Sample data - pretty self explanatory, should be easy to add to.

```
techniques:
  - jujutsu:
      stage: "trial"
      moved: "up"
      description: "Nada"

tooling:
  - claw-hammer:
      stage: "trial"
      moved: "up"
      description: "Nada"

platforms:
  - leitai:
      stage: "trial"
      moved: "up"
      description: "Nada"

languages-and-frameworks:
  - esperanto:
      stage: "trial"
      moved: "up"
      description: "Nada"
```

## Local Development

1. Install dependencies
```
npm install
```

2. Build the JSON which populates the radar

```
npm run build
```

3. Run the local server
```
npm run start
```

4. your default browser should automatically open and show the url
 
```
http://localhost:3000/
```

## License

```
The MIT License (MIT)

Copyright (c) 2017-2022 Zalando SE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
