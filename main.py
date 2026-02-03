from cloudlink import cloudlink

if __name__ == "__main__":
    cl = cloudlink()
    server = cl.server(logs=True)
    # 0.0.0.0 is required for cloud hosting (it means 'listen to everyone')
    server.run(ip="0.0.0.0", port=8080)