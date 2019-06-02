ls | while read line
do 
var=$(echo $line |sed 's/\.[^\.]*$//')#拡張子を取り除く
zip $var.zip $line
done

