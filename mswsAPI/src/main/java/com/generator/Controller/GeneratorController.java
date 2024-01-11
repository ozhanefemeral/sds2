package com.generator.Controller;

import com.generator.Generator.MiddleSquareWeylSequenceRNG;
import com.generator.Generator.RandomNumberGenerator;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin
public class GeneratorController {
    private final RandomNumberGenerator generator = new MiddleSquareWeylSequenceRNG();

    @GetMapping("/api/generate")
    public String getRandomSeq(@RequestParam int size, @RequestParam long seed) {
        return generator.generate(size, seed);
    }
}
