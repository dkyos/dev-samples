
# setup

* Install java
        * sudo add-apt-repository ppa:webupd8team/java
        * sudo apt-get update
        * sudo apt-get install -y oracle-java7-installer

* make sample file
        * $ sudo dd if=/dev/zero of=/opt/file1  bs=102410240  count=1

* run vdbench test
        * $ ./vdbench -f prf_test


* Sample configuration
```vim
sd=sd1,lun=/opt/file1
wd=rg-1,sd=sd*,rdpct=70,rhpct=0,whpct=0,xfersize=8k,seekpct=70
rd=rd_rg-1,wd=rg-1,interval=1,iorate=max,elapsed=30,forthreads=(64)
```

# Configuration

* sd - Storage Definition (where the I/O is going to/from - storage, disks, files)
* wd - Workload Definition (precise definition of workload) - some explanations:
        * rdpct - read percentage; 70 means that 70% of time is spent on reading and the rest, 30%, on writing
        * xfersize - size of each I/O
        * seekpct - percentage of random seeks
* rd - Run Definition (in general - which and for how long run Workload Definition)

