def replay(method: Callable) -> None:
    """
    Function to display the history of calls of a particular function.
    """
    history = call_history(method)
    calls = len(history)

    print(f"{method.__qualname__} was called {calls} times:")

    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)

    for call_num, (input_data, output_data) in enumerate(zip(inputs, outputs), 1):
        input_data = input_data.decode()
        output_data = output_data.decode()
        print(f"{method.__qualname__}(*{input_data}) -> {output_data}")
