
$file_count = 0;
$file_iteration = 0;

mkdir 'GCcontentOUTFILE';

$dir = "YeastGenesA"; opendir(DIR,$dir) or die "can't open directory $dir:$!"; print"\n";
#the extra function that I added to the code was that you can put in a certain DNA sequence and it will find how many times that sequence is in each file 
print "Enter a DNA sequence: ";
my $DNAseq = <>;
my $DNAseq = uc($DNAseq);
chomp($DNAseq);
my $DNAseq_counter = 0;
my $DNA_seq_position = 0; 
while($DNAseq_counter != length($DNAseq))#this while loop checks if the sequence you inputed was viable as a DNA sequence and if it is not it quits the program 
{
    my $DNAbase = substr($DNAseq, $DNA_seq_position, 1);
    if ($DNAbase eq "A" ||$DNAbase eq "T" ||$DNAbase eq "C" ||$DNAbase eq "G") {
        $DNAseq_counter++;
        $DNA_seq_position++;
    }
    else {die "You have entered an invalid sequence"}
}

while($filename = readdir DIR)
{
    $ORFname = substr($filename, 0, 7);
    print "\nmy ORF name is "."$ORFname\n";
    print OUTFILE "\nmy ORF name is "."$ORFname\n";
    $filelocation = "./YeastGenesA/"."$filename";
    if (length $ORFname == 7){
        open(INFILE, $filelocation) or die "Cannot open file";
    }else {next;}
    open (OUTFILE, ">"."./GCcontentOUTFILE/"."$filename") || die " could not open output file\n";

while(<INFILE>){
    #print "in counting while loop\n";
    chomp;
    my $totalCount = 0;
    my $CGCount = 0;
    my $DNA = <INFILE>;
    my $position = 0;
    my $DNAsize = length($DNA);
    my $counter = 0;
    my $inputed_seq_counter = 0; 
    while($DNA =~ /$DNAseq/g){$inputed_seq_counter++;}#this piece of code adds to the counter every time the previously inputed sequence is found
    while($counter !=  $DNAsize){
      my $base = substr($DNA, $position, 1);
      #print $position . "position\n";
      #print($base . "base\n");
      if($base eq "A" || $base eq "T"  || $base eq "C"  ||  $base eq "G" ){
        #print($base . "base first condition\n");
        $totalCount++;
        #print($str . "\n");
        #print $totalCount . "total Count \n";
      }
      if($base eq "G" || $base eq "C"){
        #print($base . "base second condition\n");
        $CGCount++;
        #print $CGCount . "CG count\n";
      }
      #print "$CGCount";
      $position++;
      $counter++;
    }
    #print "out of part reading to eof\n";
print "countGC "."$ORFname\t"."$CGCount\n";
print "count of inputed DNA sequence " . "$inputed_seq_counter\n";
print OUTFILE "countGC "."$ORFname\t"."$CGCount\n";
print OUTFILE "count of inputed DNA sequence " . "$inputed_seq_counter\n";
#print "countTTL "."$ORFname\t"."$totalCount\n";
#$freqGC = $CGCount/$totalCount;
#print "transLevel and freqGC "."$ORFname\t"."$transLevel\t"."$freqGC\n";
#sleep(1);
print "\n\n";
close OUTFILE;
close INFILE;
}
}
# end while loop
#question 2
#without changes my code took 5 minutes and 13 seconds to run to completion
#with my changes my code took 3 minutes and 48 seconds to run to completion 
#this means that the amount you print to screen greatly affects the speed that the program runs 

print "end program\n";
exit;
