import random
import statistics


def how_many_before_collisions(buckets, loops=1):
    """
    Roll random hashes into 'buckets' and print
    how many rolls before hash collision.

    Run 'loops' number of times
    """
    
    results = []

    for _ in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets

            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break
        
        result = tries/buckets*100
        results.append(result)

        print(
            f'{buckets} buckets, {tries} hashes before collision. ({result:.1f})')

    print(f'\nAvg {statistics.mean(results):.1f}%')

how_many_before_collisions(32, 10)