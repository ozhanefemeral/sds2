using XoshiroAPI;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Add services to the container.

var app = builder.Build();

// Configure the HTTP request pipeline.

app.MapGet("/api/generate", (string seed, string size) =>
{
    var generator = new XoshiroGenerator();
    var code = generator.Generate(seed,size);

    return TypedResults.Ok(code);

});

if(app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.Run();
