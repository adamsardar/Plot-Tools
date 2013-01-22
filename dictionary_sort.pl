#!/usr/bin/env perl -w

=head1 NAME

dictionary_sortI<.pl>

=head1 USAGE

dictionary_sort.pl [options -v,-d,-h] <ARGS> -t <delimiter sep dictionary file> -f <file to sort>
=head1 SYNOPSIS

A simple script to take a newline seperated file of values to order by and another file to sort. If the file to sort has a line that starts with the sort key, followed by whitespace, then it is outputted

Prints to STDOUT

=head1 AUTHOR

B<Adam Sardar> - I<adam.sardar@bristol.ac.uk>

=head1 COPYRIGHT

Copyright 2012 Gough Group, University of Bristol.

=cut

# Strict Pragmas
#----------------------------------------------------------------------------------------------------------------
use Modern::Perl;

# Add Local Library to LibPath
#----------------------------------------------------------------------------------------------------------------
use lib "$ENV{HOME}/bin/perl-libs-custom";

# CPAN Includes
#----------------------------------------------------------------------------------------------------------------
=head1 DEPENDANCY
B<Getopt::Long> Used to parse command line options.
B<Pod::Usage> Used for usage and help output.
B<Data::Dumper> Used for debug output.
=cut
use Getopt::Long;                     #Deal with command line options
use Pod::Usage;                       #Print a usage man page from the POD comments after __END__
use Data::Dumper;                     #Allow easy print dumps of datastructures for debugging
use List::MoreUtils qw/ uniq /;

# Command Line Options
#----------------------------------------------------------------------------------------------------------------

my $verbose; #Flag for verbose output from command line opts
my $debug;   #As above for debug
my $help;    #Same again but this time should we output the POD man page defined after __END__
my $delim = "\t";
my $dictionary_file;
my $file_to_sort;

#Set command line flags and parameters.
GetOptions("verbose|v!"  => \$verbose,
           "debug|d!"  => \$debug,
           "help|h!" => \$help,
           "delimiter|delim:s" => \$delim,
           "dict|t=s" => \$dictionary_file,
           "file|f=s" => \$file_to_sort,
        ) or die "Fatal Error: Problem parsing command-line ".$!;

#Print out some help if it was asked for or if no arguments were given.
pod2usage(-exitstatus => 0, -verbose => 2) if $help;

# Main Script Content
#----------------------------------------------------------------------------------------------------------------
open DICTIONARY, "<$dictionary_file" or die $?.$!;

my $sortorder = [];

while (my $line = <DICTIONARY>){
	chomp($line);
	die "No value found at $.\n" if($line ~~ undef);
	push(@$sortorder,$line)
}

die "Use unique sort keys!\n" unless(scalar(@$sortorder) == scalar(uniq(@$sortorder)));

close DICTIONARY;

print STDERR "Sort dictionary size = ".scalar(@$sortorder)."\n";


foreach my $sortkey (@$sortorder){

	open FILE, "<$file_to_sort" or die $!.$?;
	
	print $sortkey."\n";
	
	while (my $line = <FILE>){
		
		print $line if($line =~ m/^$sortkey\s+/);
	}
	
	close FILE
}


__END__
