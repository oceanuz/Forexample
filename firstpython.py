#!/usr/bin/env python3

# Kolakoski dizisini üretir, çıktıyı  yazdırır ve bazı istatistikler verir.


from collections import Counter
from itertools import islice

def kolakoski(n):
    """
    İlk n terimi olan Kolakoski dizisini üretir.
    Dizi 1 ve 2'lerden oluşur. Başlangıç: 1,2,2,1,1,2,1,2,2,...
    Bu fonksiyon ham bir ancak hızlı olmayan doğrusal bir üretim uygular.
    """
    if n <= 0:
        return []
    seq = [1, 2, 2]  
    i = 2  
   
    while len(seq) < n:
        run_len = seq[i]
     
        next_value = 1 if seq[-1] == 2 else 2
        seq.extend([next_value] * run_len)
        i += 1
    return seq[:n]

def pretty_print_seq(seq, width=80):
    """
    Diziyi satırlara bölerek yazdırır; yanında indeks aralıkları gösterir.
    """
    s = ''.join(str(x) for x in seq)
   
    for start in range(0, len(s), width):
        part = s[start:start+width]
        print(f"{start:6d}: {part}")

def run_statistics(seq):
    c = Counter(seq)
    runs = []
  
    prev = None
    run_len = 0
    for x in seq:
        if x == prev:
            run_len += 1
        else:
            if prev is not None:
                runs.append((prev, run_len))
            prev = x
            run_len = 1
    if prev is not None:
        runs.append((prev, run_len))
    run_lengths = [rl for (_v, rl) in runs]
    rl_count = Counter(run_lengths)
    return {
        'counts': dict(c),
        'total_terms': len(seq),
        'num_runs': len(runs),
        'run_length_distribution': dict(sorted(rl_count.items()))
    }

def main():
    print("Kolakoski Dizisi — kendini üreten 1/2 dizisi\n")
    N = 300 
    seq = kolakoski(N)
    print(f"İlk {N} terim:\n")
    pretty_print_seq(seq, width=100)
    print("\nİstatistikler:")
    stats = run_statistics(seq)
    print(f" Toplam terim: {stats['total_terms']}")
    print(f" 1 sayısı: {stats['counts'].get(1,0)}")
    print(f" 2 sayısı: {stats['counts'].get(2,0)}")
    print(f" Koşu (run) sayısı: {stats['num_runs']}")
    print(" Koşu uzunluğu dağılımı (uzunluk: frekans):")
    for length, freq in stats['run_length_distribution'].items():
        print(f"  {length:2d} : {freq}")

   
    print("\nKoşu görselleştirmesi (her koşu bir sembol kümesi):")
    viz = ''.join('#' * l if v == 1 else '.' * l for v, l in 
                  [(v, l) for v, l in ([ (vv, ll) for vv,ll in [] ])])  
   
    runs = []
    prev = None
    run_len = 0
    for x in seq:
        if x == prev:
            run_len += 1
        else:
            if prev is not None:
                runs.append((prev, run_len))
            prev = x
            run_len = 1
    if prev is not None:
        runs.append((prev, run_len))
  
    short_viz = []
    for v, l in runs[:80]: 
        short_viz.append(('#' * l) if v == 1 else ('.' * l))
    print(''.join(short_viz))
    print("\n(Not: '#' = 1'in koşusu, '.' = 2'nin koşusu)\n")
    print("Kolakoski dizisi hakkında daha fazla ilginç soru:")
    print(" - Sınırlı bir orana (1'lerin oranı) sahip mi? (açık bir ispat yok)")
    print(" - Dizinin kendi kendini üretme mekanizması sebebiyle birçok açık problem bulunuyor.")
    print("\nDosyayı GitHub'a eklemek için README'ye kısa açıklama ekleyebilirsiniz.")

if __name__ == "__main__":
    main()
