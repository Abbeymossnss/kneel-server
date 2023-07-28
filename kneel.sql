CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY, AUTOINCREMENT
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY, AUTOINCREMENT
    `carets` NUMERIC(2,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY, AUTOINCREMENT
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY, AUTOINCREMENT
    `style_id` NVARCHAR(160) NOT NULL,
    `metal_id` NUMERIC(5,2) NOT NULL,
    `size_id` NUMERIC(5,2) NOT NULL,
    FOREIGN KEY(`style_id`) REFERENCES `Style`(`id`),
	FOREIGN KEY(`metal_id`) REFERENCES `Metal`(`id`)
    FOREIGN KEY(`size_id`) REFERENCES `Size`(`id`)
);

INSERT INTO `Metal` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metal` VALUES (null, "14K Gold", 736.40);
INSERT INTO `Metal` VALUES (null, "24K Gold", 1258.90);
INSERT INTO `Metal` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metal` VALUES (null, "Paladium", 1241.00);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1.0, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2.0, 3638);

INSERT INTO `Style` VALUES (null, "Classic", 500);
INSERT INTO `Style` VALUES (null, "Modern", 710);
INSERT INTO `Style` VALUES (null, "Vintage", 965);

INSERT INTO `Order` VALUES (null, 1, 1, 1);
INSERT INTO `Order` VALUES (null, 1, 3, 4);
INSERT INTO `Order` VALUES (null, 2, 1, 1);
INSERT INTO `Order` VALUES (null, 1, 2, 2);
INSERT INTO `Order` VALUES (null, 2, 3, 1);
INSERT INTO `Order` VALUES (null, 2, 3, 1);
INSERT INTO `Order` VALUES (null, 1, 4, 2);
INSERT INTO `Order` VALUES (null, 1, 4, 2);
INSERT INTO `Order` VALUES (null, 2, 2, 1);
INSERT INTO `Order` VALUES (null, 2, 3, 2);


SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    m.metal metal_name,
    m.price metal_price,
    s.style style_style,
    s.price style_price,
    z.carets size_carets,
    z.price size_price
    FROM `Order` o
    JOIN Metal m
            ON m.id = o.metal_id
    JOIN Style  s
            ON s.id = o.style_id
    JOIN Size z
            ON z.id = o.size_id


SELECT
    o.id,
    o.metal_id,
    o.size_id,
    o.style_id,
    m.metal metal_name,
    m.price metal_price,
    s.style style_style,
    s.price style_price,
    z.carets size_carets,
    z.price size_price
FROM `Order` o
JOIN Metal m
        ON m.id = o.metal_id
JOIN Style  s
        ON s.id = o.style_id
JOIN Size z
        ON z.id = o.size_id
WHERE o.id = 2









