#! /usr/bin/env perl

=head1 NAME
dictionary_converterI<.pl>

=head1 USAGE

dictionary_converter.pl [options -v,-d,-h] <ARGS> -t <delimiter sep dictionary file> -f <file to translate 'from to'> (*opt -delim <delimter>) (-i --invert command line flag to invert the dictionary file, 'from to' becomes 'to from')

=head1 SYNOPSIS

A simple script to take a *delimiter* seperated file of values to translate (from	to\n) and a file to translate. The delimeter is by default tab ("\t"), but this can be easily changed using -delim.
Prints to STDOUT

=head1 AUTHOR

B<Adam Sardar> - I<adam.sardar@bristol.ac.uk>

=head1 COPYRIGHT

Copyright 2011 Gough Group, University of Bristol.

=cut

# CPAN Includes
#----------------------------------------------------------------------------------------------------------------
=head1 DEPENDANCY
B<Getopt::Long> Used to parse command line options.
B<Pod::Usage> Used for usage and help output.
B<Data::Dumper> Used for debug output.
=cut
use Modern::Perl;
use Getopt::Long;                     #Deal with command line options
use Pod::Usage;                       #Print a usage man page from the POD comments after __END__
use Data::Dumper;                     #Allow easy print dumps of datastructures for debugging

# Command Line Options
#----------------------------------------------------------------------------------------------------------------

my $verbose; #Flag for verbose output from command line opts
my $debug;   #As above for debug
my $help;    #Same again but this time should we output the POD man page defined after __END__
my $delim = "\t";
my $dictionary_file;
my $file_to_translate;
my $invert;

#Set command line flags and parameters.
GetOptions("verbose|v!"  => \$verbose,
           "debug|d!"  => \$debug,
           "help|h!" => \$help,
           "delimiter|delim:s" => \$delim,
           "dict|t=s" => \$dictionary_file,
           "file|f=s" => \$file_to_translate,
           "invert|i!" => \$invert,
        ) or die "Fatal Error: Problem parsing command-line ".$!;

#Print out some help if it was asked for or if no arguments were given.
pod2usage(-exitstatus => 0, -verbose => 2) if $help;

# Main Script Content
#----------------------------------------------------------------------------------------------------------------

open DICTIONARY, "<$dictionary_file" or die $?.$!;

my $dictionary_hash = {};


unless($invert){
	while (my $line = <DICTIONARY>){
		chomp($line);
		my ($key,$value) = split(/$delim/,$line);
		die "No value found for $key\n" if($value ~~ undef);
		$dictionary_hash->{$key}=$value;
	}
}else{
	while (my $line = <DICTIONARY>){
		chomp($line);
		my ($value,$key) = split(/$delim/,$line);
		die "No value found for $key\n" if($value ~~ undef);
		$dictionary_hash->{$key}=$value;
		
	}
}

close DICTIONARY;

print STDERR "dictionary size = ".scalar(keys(%$dictionary_hash))."\n";

print STDERR join("\t",keys(%$dictionary_hash)) if $verbose;

open FILE, "<$file_to_translate" or die $!.$?;

while (my $line = <FILE>){
	
	chomp($line);	

	foreach my $word2translate (keys(%$dictionary_hash)){
		#print $word2translate."\n";
		my $translation = $dictionary_hash->{$word2translate};
		#print $translation."\n";
		$line =~ s/\b$word2translate\b/$translation/g;
	}

	print $line."\n";
}

close FILE

__END__
