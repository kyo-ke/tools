ls | while read line
do 
var=$(echo $line |sed 's/\.[^\.]*$//')
zip $var.zip $line
done

