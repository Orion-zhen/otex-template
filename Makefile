.PHONY: clean

# 想要一次性删除的文件模式
CLEAN_FILES := *.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.nav *.out *.pdf *.snm *.toc *.xdv
# 想要一次性删除的目录
CLEAN_DIRS  := build/ _minted/

clean:
	@echo "Cleaning LaTeX auxiliary files..."
	rm -f $(CLEAN_FILES)
	rm -rf $(CLEAN_DIRS)
	@echo "Clean complete."