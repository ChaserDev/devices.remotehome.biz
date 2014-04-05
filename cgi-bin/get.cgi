#!/usr/bin/perl

# PERL MODULES WE WILL BE USING
use DBI;
use DBD::mysql;

local ($buffer, @pairs, $pair, $name, $value, %FORM);
    # Read in text
    $ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    if ($ENV{'REQUEST_METHOD'} eq "GET")
    {
	$buffer = $ENV{'QUERY_STRING'};
    }
    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%(..)/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
    }
    $first_name = $FORM{first_name};
    $last_name  = $FORM{last_name};

# HTTP HEADER
print "Content-type: text/html \n\n";

# CONFIG VARIABLES
$platform = "mysql";
$database = "remotehome_devices";
$host = "localhost";
$port = "3306";
$tablename = "devices";
$user = "charlal1";
$pw = "rndm8274";

# DATA SOURCE NAME
$dsn = "dbi:mysql:$database:localhost";

# PERL DBI CONNECT
$connect = DBI->connect($dsn, $user, $pw);

# PREPARE THE QUERY
$query = "INSERT INTO devices (first_name, last_name) VALUES ('$first_name','$last_name')";
$query_handle = $connect->prepare($query);

# EXECUTE THE QUERY
$query_handle->execute();

print "Done";
