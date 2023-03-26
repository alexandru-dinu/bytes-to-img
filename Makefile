%.bin: %.c
	gcc -o $@ $^
	strip $@

.PHONY: clean
clean:
	rm -f *.bin *.png
	rm -rf .mypy_cache
