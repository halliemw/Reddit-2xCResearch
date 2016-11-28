This package presumes:

One .txt file = one document
All documents exist in a single folder
That you know how to point to.

You'll want at least a few hundred documents to get anything reasonable out of this thing.

Topic modeling is mean to be a distant reading guide to help oint you to the close reading that you want to do.

You can set the number of topics that it will work with.  Try 10 and 30.  You may have to find a sweet spot in the middle, depending on the diversity of your collection and sheer volume of documents that you are working with.  The program cannot suggest an ideal number of topics.  You'll need to experiment and find one on your own.

This python script will launch some java stuff.  If you start getting heap errors in terminal you're running out of ram.  Pester someone for some cluster access and time or find a sysadmin in the library who can loan you a beefy desktop.  I suppose that you could get this to work on windows.  It will be painful.  Get a linux system.  You'll need to have Python 2.x and java available.  Which you should on a mac.  You shouldn't need to install anything separately for this.  All the packages that the python script uses are standard library things.

It won't run on multiple processors, but it can still be run on a cluster.  Don't let anyone give you shit.

Alternatively, you can securely send me your documents and I can run this bad boy on my end and send you the results.  Collaboration, right?

Have you considered patron privacy?

What I'm passing to you includes all my original results and a teeny version of the documents so you can at least test it on something that you know will work.  You won't need to do any special formatting with the documents, but they should be plain txt files.  That means NO markup.  NO xml.  NO html.  You'll want to also strip out any meta information, particularly out of chat logs.  You might consider stripping out just the text from the library and just the text from the patrons and run those independently through the program just to see the diffs between them.  Check if that influences any differences when running it over the complete logs.  

You'll need to change several places within the dotopicmodel.py file to get it going:

Line 9:  change this to the path of where the documents live.  Can be full or relative.
Line 18:  change this to the number of topics you want.  Leave as a string.
Line 24:  name the project, this will be the file name of the output.  make this unique each time or you'll overwrite your junk.

To run the script:

Inside of terminal, navigate to the folder containing dotopicmodel.py.  Exce