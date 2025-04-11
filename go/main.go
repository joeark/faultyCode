package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, `{"status": "ok"}`)
	})

	fmt.Println("Server starting on :8080")
	http.ListenAndServe(":8080", nil)
}
