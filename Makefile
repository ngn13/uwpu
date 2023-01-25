build/uwpu.exe: src/uwpu.go
	GOOS=windows GOARCH=amd64 go build -o $@ $^

clean:
	rm -rf build