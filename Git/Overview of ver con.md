
### version control
https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
- Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later
-  allows you to revert selected files back to a previous state
-  revert the entire project back to a previous state,
-  compare changes over time
-  see who last modified something that might be causing a problem.
-  who introduced an issue and when, and more.

### Local Version Control Systems
- copy files into another directory
- This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you’re in and accidentally write to the wrong file or copy over files you don’t mean to.
- lvcs ex: rcs works by keeping patch sets,(that is, the differences between files)

### Centralized Version Control Systems
-  Have a single server that contains all the versioned files, and a number of clients that check out files from that central place. 
-  This setup offers many advantages, especially over local VCSs. For example, everyone knows to a certain degree what everyone else on the project is doing.
-  The most obvious is the single point of failure that the centralized server represents


### Distributed Version Control Systems
- clients don’t just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history
-  Thus, if any server dies, and these systems were collaborating via that server, any of the client repositories can be copied back up to the server to restore it.
-   so you can collaborate with different groups of people in different ways simultaneously within the same project. 
-  This allows you to set up several types of workflows that aren’t possible in centralized systems, such as hierarchical models.
