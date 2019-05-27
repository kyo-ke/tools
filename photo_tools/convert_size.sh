for file in $(find *.png)
do
    convert $file -resize 96x96 ../re_test/n_$file
done