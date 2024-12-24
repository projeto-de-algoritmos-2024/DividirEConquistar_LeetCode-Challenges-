# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Media of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        numsFinal = nums1 + nums2

        def mediana_medianas(arr, target):
            def dividir_grupos(arr):
                return [arr[i:i+5] for i in range(0, len(arr), 5)] # divide em grupos de 5 dentro do nosso arr
            
            def encontra_mediana(grupo):
                grupo.sort()
                return grupo[len(grupo)//2]
            
            # Faz toda aquela parte de dividir e encontrar a mediana
            grupos_divididos = dividir_grupos(arr)
            mediana = [encontra_mediana(grupo) for grupo in grupos_divididos]

            if len(mediana) <= 5:
                mediana.sort()
                pivo = mediana[len(mediana) // 2]
            else:
                pivo = mediana_medianas(mediana, len(mediana) // 2)
            
            # Faz a parte de determinar os elementos que são maiores e são menores que o pivô encontrado
            menores = [x for x in arr if x < pivo]
            maiores = [x for x in arr if x > pivo]
            pivos = [x for x in arr if x == pivo]

            if target < len(menores):
                return mediana_medianas(menores, target)
            elif target < len(menores) + len(pivos): 
                return pivo
            else:
                return mediana_medianas(maiores, target - len(menores) - len(pivos)) 

        tam_arr = len(numsFinal) # tamanho final ao mesclar

        if tam_arr % 2 == 1: # caso seja par o tamanho
            return mediana_medianas(numsFinal, tam_arr // 2)
        else: # caso seja ímpar o tamanho
            return (mediana_medianas(numsFinal, tam_arr // 2 - 1) + mediana_medianas(numsFinal, tam_arr // 2)) / 2.0