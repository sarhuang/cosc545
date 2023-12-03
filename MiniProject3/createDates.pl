use strict;
use warnings;


my $t = 1697117340;
my $int = 3600*24*14;
$t -= $int;


print "|id|from|to|\n|-|-|-|\n";

open A, "list";
while (<A>){
  chop();
  my $u = $_;
  my @vals = localtime($t);
  $vals[4] += 1;
  for my $i (0..5){
	  $vals[$i] = fix ($vals[$i]);
  }
  my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = @vals;
  $year += 1900;

  $t-=$int;
  @vals = localtime($t);
  $vals[4] += 1;
  for my $i (0..5){
	  $vals[$i] = fix ($vals[$i]);
  }
  my ($sec1, $min1, $hour1, $mday1, $mon1, $year1, $wday1, $yday1, $isdst1) = @vals;
  $year1 += 1900;
  print "|$u|$year1-$mon1-${mday1}T$hour1:$min1:$sec1.000|$year-$mon-${mday}T$hour:$min:$sec.000|\n";
  $t-=$int;
}

sub fix {
	my $v = $_[0];
   $v = "0$v" if $v<10;
   $v;
}