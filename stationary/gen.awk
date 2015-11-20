BEGIN {
    id = 1;
    print "{[";
}
/[^=]*=[0-9]+/{
    print "\t{";
    print "\t\t\"id\":", id++ ",";
    print "\t\t\"name\":", "\"" $1 "\"" ",";
    print "\t\t\"total\":", $2 ",";
    print "\t\t\"left\":", $2;
    print "\t},";
}
END {
    print "]}";
}
