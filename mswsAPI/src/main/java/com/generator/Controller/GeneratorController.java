package com.generator.Controller;

import com.generator.Generator.MiddleSquareWeylSequenceRNG;
import com.generator.Generator.RandomNumberGenerator;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GeneratorController {
    private final RandomNumberGenerator generator = new MiddleSquareWeylSequenceRNG();

    @GetMapping("/api/generate")
    public String getRandomSeq() {
        return generator.generate(1000);
    }
}
