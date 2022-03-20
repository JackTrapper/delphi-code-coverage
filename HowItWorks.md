A code coverage tool for Delphi 2010
====================================

Prelude…
---------

My day job is [squarely in the Java world](http://coherence.oracle.com/display/INCUBATOR/Home), and trust me, in many respects it is a wonderful world. The amount of high quality, free, open source tools surrounding the Java platform is enormous. For someone interested not only in development but in “software engineering”, there is a risk that you spend all your time exploring all the great tools instead of doing some productive work…

Now, in the past professionally, and recently[as a hobby](http://www.whatsrunning.net/), I have been using Borland/Embarcadero tools ranging from [Turbo Pascal for Windows](http://en.wikipedia.org/wiki/Turbo_Pascal) back in 1993 (who remembers TPW 1.0, hands up?) up to Delphi 2010. The Delphi community and the range of free libraries and tools has always been good, if not great. Delphi has been a very “complete” environment for the traditional Windows client and I’d say many Delphi developers probably feel uncomfortable leaving their IDE to use another tool. This has been different for other languages like C++ or Java where weaker development environments have had to be compensated by a range of IDE external tools. As far as a development IDE, Delphi is still very competitive.

As software engineering practices have advanced, a lot of the tooling focus has moved out from the developers IDE to the Continuous Integration system. With the advent of good tooling to support CI, the discipline of software engineering has taken a huge step from the closets of University CS departments out to the world of enterprise software development. Many are the development teams who embrace agile practices (code word:scrum), TDD and metrics driven development. One (in my view) welcome aspect of this is that the responsibility for quality has to a very large degree moved to the development team from the (usually understaffed) QA function. The whole point of Continuous Integration is to stay focused on the goal of having a quality product. And today, honestly, I’d think that a development shop who doesn’t use a CI tool like [Hudson](http://www.hudson-ci.org/) is seriously behind the times.

Now as people start using [Hudson to build Delphi projects](https://christerblog.wordpress.com/2010/04/25/using-hudson-to-build-delphi-projects/) I know that people (at least I do) desire the same level of quality introspection and visibility in to their Delphi projects as they have with their Java, .Net and C++ projects. If that doesn’t materialize, the viability of Delphi as a development tool will diminish.

So – what’s missing you might ask?

Here’s my list:

- An open source code coverage tool for Delphi
- Static code analysis tools to find bugs and enforce coding guidelines (yes I love CTRL-D in Delphi 2010!)
- Advanced mocking framework to facilitate unit testing
- Hudson plugin to parse and visualize Delphi compiler output properly
- Hudson plugin to parse and visualize DUnit output (or alternatively adopt DUnit to what JUnit outputs)
- Hudson plugin to keep track of code coverage for tests

I understand that [Embarcadero](https://christerblog.wordpress.com/2010/06/25/a-code-coverage-tool-for-delphi-2010/www.embarcadero.com) has embraced Hudson as a CI tool themselves – why not create and release some Delphi specific Hudson plugins, Embarcadero?

Introducing Delphi Code Coverage
--------------------------------

So with that way too long prelude (still reading?) – to the point of this article. I have just submitted a new open source project to Google code called [Delphi Code Coverage](http://code.google.com/p/delphi-code-coverage/) and it is to my knowledge the only free code coverage tool for Delphi. I’ve had this tool lingering on my hard drive in an unfinished state for a year and decided to spend a few hours to polish it up well enough to release it to the world. The inspiration comes again from the Java world where I have been using [Emma](http://emma.sourceforge.net/) as my code coverage tool of choice for quite some time.

Right now the tool only does line coverage, i.e. it will keep track of what lines were executed and visualize that in an html report. So you could say that it is an embryo of a Code coverage tool compared to mature code coverage tools out there. **With some luck,** this is a tool that more people would be willing to invest some time in and help make it as awesome as the awesome Delphi community deserves. There are plenty of features to implement to match the state of the art in Code Coverage tooling…

How it works and what does it do
---------------------------------

[Delphi Code Coverage](http://code.google.com/p/delphi-code-coverage/) is a command line tool that will run your executable and using the accompanying detailed MAP file keep track of what source lines were executed.

Here is a sample ( I hope self-explanatory):

    CodeCoverage -e TestApp.exe -m TestApp.map -u TestUnit AnotherUnit AThirdUnit
    
This command line will generate 4 html files, three for the units you supplied and one with a summary for all the supplied units.

More details on the usage is available in the readme.

That’s all folks for now. I hope you give the tool a spin and let me know what you think!
