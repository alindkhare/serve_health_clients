package main

import (
	"github.com/nahid/gohttp"
	"fmt"
	"os"
)

func main() {
	patient_name := os.Args[1]
	ip := os.Args[2]
	fmt.Println(patient_name,ip)
	address := "http://"+ip+"/hospital?patient_name="+patient_name+"&value=0.0&vtype=ECG"
	fmt.Println(address)

	req := gohttp.NewRequest()
	ch := make(chan *gohttp.AsyncResponse)
	totalRequest := 3750
	for i := 0; i <= totalRequest; i++ {
		req.FormData(map[string]string{"user": ""}).AsyncGet(address,ch)
	}
	for i:=0; i<= totalRequest; i++ {
		op := <-ch

		fmt.Println(op)
	}

}