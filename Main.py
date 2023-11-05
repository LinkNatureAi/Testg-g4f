import g4f, asyncio

_providers = [
    g4f.Provider.Bard,
    g4f.Provider.Liaobots,
    g4f.Provider.Raycast,
    g4f.Provider.AItianhu,
    g4f.Provider.ChatgptDemo,
    g4f.Provider.ChatgptFree,
    g4f.Provider.FreeGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.Llama2,
	
    g4f.Provider.GeekGpt,
    g4f.Provider.Myshell,
    g4f.Provider.ChatgptAi,
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.Bing,
    g4f.Provider.GptGo,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
]

async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Hello"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)
        
async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)

asyncio.run(run_all())
