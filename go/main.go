package main

import (
	"net/http"
)

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(200)
		fmt.Fprint(w, `{"status": "ok"}`)
	})

	fmt.Println("Server starting on :8080")
	http.ListenAndServe(":8080", nil)
}