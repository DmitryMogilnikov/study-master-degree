package main

import (
	"fmt"
	"math"
	"os"
	"sync"
)

func main() {
	// Открытие файла с числами для чтения
	file, err := os.Open("notebooks/02. multiprocessing.ipynb/random_numbers32.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close() // Закрывает файл после завершения main

	var wg sync.WaitGroup
	totalPrimes := make(chan int)

	// Запуск горутины для каждого числа из файла
	for {
		var n int
		_, err := fmt.Fscanf(file, "%d\n", &n)
		if err != nil {
			break
		}

		wg.Add(1)
		go func(num int) {
			defer wg.Done()
			factors := primeFactors(num)
			totalPrimes <- len(factors)
		}(n)
	}

	// Закрытие канала totalPrimes после завершения всех горутин
	go func() {
		wg.Wait()
		close(totalPrimes)
	}()

	// Суммирование результатов, полученных из канала totalPrimes
	var sum int
	for count := range totalPrimes {
		sum += count
	}

	fmt.Printf("Суммарное количество простых множителей: %d\n", sum)
}

// Функция для нахождения простых множителей числа n
func primeFactors(n int) []int {
	var factors []int
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		for n%i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}
