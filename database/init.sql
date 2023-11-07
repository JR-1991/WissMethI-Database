CREATE TABLE `mixtures`.`mixtures` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `mixtures`.`density` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `density` DECIMAL(12,4) NULL,
  `mol_fraction_water` DECIMAL(5,4) NULL,
  `temperature` DECIMAL(7,4) NULL,
  `literature_doi` VARCHAR(1000) NULL,
  `mixture_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mixture_density_idx` (`mixture_id` ASC),
  CONSTRAINT `fk_mixture_density`
    FOREIGN KEY (`mixture_id`)
    REFERENCES `mixtures`.`mixtures` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS `mixtures`.`viscosity` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `viscosity` DECIMAL(12,4) NULL,
  `mol_fraction_water` DECIMAL(5,4) NULL,
  `temperature` DECIMAL(7,4) NULL,
  `literature_doi` VARCHAR(1000) NULL,
  `mixture_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mixture_viscosity_idx` (`mixture_id` ASC),
  CONSTRAINT `fk_mixture_viscosity`
    FOREIGN KEY (`mixture_id`)
    REFERENCES `mixtures`.`mixtures` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);