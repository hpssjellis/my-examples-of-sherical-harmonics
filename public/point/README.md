



prompt for llm



Act as a JSON file generator. Your task is to output a single, complete JSON object containing the coordinate data for a 3D point cloud, formatted for a JavaScript application.

The resulting JSON object MUST strictly adhere to the following structure:

1.  **"metadata"**: A string describing the file content.
2.  **"vertexCount"**: A number representing the total count of vertices in the positions array (total elements divided by 3).
3.  **"segments"**: An object containing two properties, "width" and "height", both set to the number 32.
4.  **"positions"**: A single, flat array of floating-point numbers. This array must contain the X, Y, and Z coordinates for every vertex in the point cloud, sequentially: [X1, Y1, Z1, X2, Y2, Z2, ...].

The point cloud object you must generate is a **Perfect Sphere** with a **Radius of 50**.

The sphere is defined by **32 width segments** and **32 height segments**. Therefore, the total number of vertices must be 1089 ((32 + 1) * (32 + 1)).

You must calculate and output the exact X, Y, and Z coordinates for all **1089 vertices** that form the surface of a perfect sphere of radius 50, given those segment counts. The final "positions" array will contain exactly **3267** (1089 * 3) floating-point numbers.

**Output ONLY the complete, valid JSON object, starting with the opening curly brace, and nothing else.**
