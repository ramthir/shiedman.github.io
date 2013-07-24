ASSET=assets/css
OBJ=$(ASSET)/site.css
less_file=less/site.less
md_files := $(shell find _posts  -type f -name "*.md")
$(OBJ): $(less_file) less/custom.variables.less
	lessc $(less_file) $(OBJ)

done: $(md_files)
	echo $(md_files)>done

all: $(OBJ)

