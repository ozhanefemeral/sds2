package com.generator.Controller;

import com.generator.Generator.MiddleSquareWeylSequenceRNG;
import com.generator.Generator.RandomNumberGenerator;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin
public class GeneratorController {
    private final RandomNumberGenerator generator = new MiddleSquareWeylSequenceRNG();

    @GetMapping("/api/generate")
    public String getRandomSeq(@RequestParam int size, @RequestParam long seed) {
        return "\""+generator.generate(size, seed)+"\"";
    }
}
