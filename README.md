# Zalando Tech Radar

The [Zalando Tech Radar](http://zalando.github.io/tech-radar) helps our teams make the right technology choices. 
It reflects the current consensus of the Technology Guild at Zalando and is updated quarterly.
It is of course inspired by the [ThoughtWorks Tech Radar](http://www.thoughtworks.com/radar/).

The visualization is based on [protovis](http://mbostock.github.io/protovis/) and was originally developed by [Brett Dargan](https://github.com/bdargan/techradar).

## Cool, how can I create my own?

Create a google doc with the following columns:

* **Technology** (e.g. "Hystrix")
* **Quadrant** (e.g. "Platforms & Infrastructure")
* *[optional] Comments (e.g. "lib for fault tolerance")* 
* **Score** as a float between -2 and 2 (e.g. "1.8")
* *[optional] Number of votes, for internal bookkeeping*
* *[optional] Consensus, for internal bookkeeping*
* **Skip** &mdash; set to true if entry should not be visualized on chart

Then, follow the instructions below:

## How to generate a new chart

1. on master google doc, select `File > Download as > Tab-separated values` and store as `data/year-month.tsv`
2. run `gem install liquid` if necessary
3. run `./transform.rb` to generate a new `radar_data.js`
4. open `index.html` in browser to inspect the result
5. repeat the last two steps until you're happy with the arrangement
6. check everything in
7. merge `master` branch into `gh-pages`
8. push `gh-pages` to publish the new radar 

## License
Apache 2.0 &mdash; same as [bdargan/techradar](https://github.com/bdargan/techradar)




