package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

type Tool struct {
	name string
	url  string
}

func check(err error, errs string) {
	if err != nil {
		log.Fatal(errs)
	}
}

func download(file string, path string) {
	out, err := os.Create(file)
	check(err, "Cannot create the file: "+file)
	defer out.Close()

	resp, err := http.Get(path)
	check(err, "Cannot GET: "+path)
	defer resp.Body.Close()

	_, err = io.Copy(out, resp.Body)
	check(err, "Cannot write to the file: "+file)
}

func listTools(tools []Tool) {
	log.Println("Avaliable tools:")
	for i, el := range tools {
		if i != len(tools)-1 {
			fmt.Print(el.name + ", ")
		} else {
			fmt.Print(el.name + "\n")
		}
	}
}

func main() {
	log.SetFlags(0)

	tools := []Tool{
		Tool{"winpeas.exe", "https://github.com/carlospolop/PEASS-ng/releases/download/20230122/winPEASany.exe"},
		Tool{"privesccheck.ps1", "https://raw.githubusercontent.com/itm4n/PrivescCheck/master/PrivescCheck.ps1"},
		Tool{"ncat.zip", "https://nmap.org/dist/ncat-portable-5.59BETA1.zip"},
		Tool{"accesschk.zip", "https://download.sysinternals.com/files/AccessChk.zip"},
		Tool{"accessenum.zip", "https://download.sysinternals.com/files/AccessEnum.zip"},
	}

	self := os.Args[0]

	if len(os.Args) != 2 {
		log.Println("Usage: " + self + " <tool>")
		listTools(tools)
		return
	}

	tool := os.Args[1]

	found := false
	var toolst Tool
	for _, el := range tools {
		if el.name == tool {
			found = true
			toolst = el
		}
	}

	if !found {
		listTools(tools)
		log.Fatal("Tool not found: " + tool)
	}

	log.Println("Downloading " + toolst.name + "...")
	download(toolst.name, toolst.url)
	log.Println("Success!")
}
