-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 30-05-2018 a las 15:38:32
-- Versión del servidor: 10.1.31-MariaDB
-- Versión de PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `acruz`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_asignacionactivo`
--

CREATE TABLE `anuario_asignacionactivo` (
  `bindex_id` int(11) NOT NULL,
  `red_bono` double DEFAULT NULL,
  `red_efectivo` double DEFAULT NULL,
  `red_convertible` double DEFAULT NULL,
  `red_preferida` double DEFAULT NULL,
  `red_acciones` double DEFAULT NULL,
  `red_otra` double DEFAULT NULL,
  `portafolio_fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_bindex`
--

CREATE TABLE `anuario_bindex` (
  `id` int(11) NOT NULL,
  `morningstar_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_branding`
--

CREATE TABLE `anuario_branding` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_broadcategory`
--

CREATE TABLE `anuario_broadcategory` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_carteracliente`
--

CREATE TABLE `anuario_carteracliente` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `monto` int(11) NOT NULL,
  `bindex_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `tipoInversion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_categoria`
--

CREATE TABLE `anuario_categoria` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `broadCategory_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `moneda_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_claseactivo`
--

CREATE TABLE `anuario_claseactivo` (
  `bindex_id` int(11) NOT NULL,
  `datos` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_cliente`
--

CREATE TABLE `anuario_cliente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_countryexposure`
--

CREATE TABLE `anuario_countryexposure` (
  `bindex_id` int(11) NOT NULL,
  `country_exposure` longtext COLLATE utf8_unicode_ci,
  `country_exposure_bond` longtext COLLATE utf8_unicode_ci,
  `country_exposure_convertible` longtext COLLATE utf8_unicode_ci,
  `country_exposure_equity` longtext COLLATE utf8_unicode_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_domicilio`
--

CREATE TABLE `anuario_domicilio` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_fondo`
--

CREATE TABLE `anuario_fondo` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nombre_legal` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `categoria_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `domicilio_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `moneda_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_frecuenciadistribucion`
--

CREATE TABLE `anuario_frecuenciadistribucion` (
  `id` int(11) NOT NULL,
  `frecuencia` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_instrumento`
--

CREATE TABLE `anuario_instrumento` (
  `bindex_id` int(11) NOT NULL,
  `run_svs` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `clase_proveedor` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `operation_ready` int(11) DEFAULT NULL,
  `branding_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fondo_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `frecuenciaDistribucion_id` int(11) DEFAULT NULL,
  `proveedor_id` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rendimiento_id` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tipoInstrumento_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_moneda`
--

CREATE TABLE `anuario_moneda` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_movimiento`
--

CREATE TABLE `anuario_movimiento` (
  `id` int(11) NOT NULL,
  `monto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `numero_cuotas` int(11) NOT NULL,
  `bindex_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `tipoInversion_id` int(11) NOT NULL,
  `tipoMovimiento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_pais`
--

CREATE TABLE `anuario_pais` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_ing` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_precio_actual`
--

CREATE TABLE `anuario_precio_actual` (
  `bindex_id` int(11) NOT NULL,
  `DayEndNAVDate` date DEFAULT NULL,
  `DayEndNAV` double DEFAULT NULL,
  `MonthEndNAVDate` date DEFAULT NULL,
  `MonthEndNAV` double DEFAULT NULL,
  `UnsplitNAV` double DEFAULT NULL,
  `NAV52wkHigh` double DEFAULT NULL,
  `NAV52wkHighDate` date DEFAULT NULL,
  `NAV52wkLow` double DEFAULT NULL,
  `NAV52wkLowDate` date DEFAULT NULL,
  `PerformanceReturnSource` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `CurrencyISO3_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_proveedor`
--

CREATE TABLE `anuario_proveedor` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `datos` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_rendimiento`
--

CREATE TABLE `anuario_rendimiento` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_rentabilidad`
--

CREATE TABLE `anuario_rentabilidad` (
  `bindex_id` int(11) NOT NULL,
  `DayEndDate` date DEFAULT NULL,
  `DayEndNAV` double DEFAULT NULL,
  `NAVChange` double DEFAULT NULL,
  `NAVChangePercentage` double DEFAULT NULL,
  `Retorno` longtext COLLATE utf8_unicode_ci,
  `Rank` longtext COLLATE utf8_unicode_ci,
  `CategoryEndDate` date DEFAULT NULL,
  `CategoryReturn` longtext COLLATE utf8_unicode_ci,
  `CategorySize` longtext COLLATE utf8_unicode_ci,
  `PricingFrequency` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fondo_id` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_rentafija`
--

CREATE TABLE `anuario_rentafija` (
  `bindex_id` int(11) NOT NULL,
  `bsed` double NOT NULL,
  `bsem` double NOT NULL,
  `bsmd` double NOT NULL,
  `bsym` double NOT NULL,
  `cred` double NOT NULL,
  `crem` double NOT NULL,
  `crmd` double NOT NULL,
  `crym` double NOT NULL,
  `portafolio_fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_reporte_anual_couta`
--

CREATE TABLE `anuario_reporte_anual_couta` (
  `bindex_id` int(11) NOT NULL,
  `AnnualReportDate` date DEFAULT NULL,
  `NetExpenseRatio` double DEFAULT NULL,
  `AnnualReportPerformanceFee` double DEFAULT NULL,
  `InterimNetExpenseRatioDate` date DEFAULT NULL,
  `InterimNetExpenseRatio` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_saldoactualizado`
--

CREATE TABLE `anuario_saldoactualizado` (
  `id` int(11) NOT NULL,
  `monto` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `bindex_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `tipoInversion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_saldomensual`
--

CREATE TABLE `anuario_saldomensual` (
  `id` int(11) NOT NULL,
  `anio` int(11) NOT NULL,
  `mes` int(11) NOT NULL,
  `saldoCierre` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `tipoInversion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_sector`
--

CREATE TABLE `anuario_sector` (
  `bindex_id` int(11) NOT NULL,
  `materiales_basicos` double DEFAULT NULL,
  `servicio_comunicacion` double DEFAULT NULL,
  `ciclico_consumidor` double DEFAULT NULL,
  `defensa_consumidor` double DEFAULT NULL,
  `energia` double DEFAULT NULL,
  `servicios_financieros` double DEFAULT NULL,
  `cuidado_salud` double DEFAULT NULL,
  `acciones_industriales` double DEFAULT NULL,
  `bienes_raices` double DEFAULT NULL,
  `tecnologia` double DEFAULT NULL,
  `utilidades` double DEFAULT NULL,
  `portafolio_fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipoinstrumento`
--

CREATE TABLE `anuario_tipoinstrumento` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipoinversion`
--

CREATE TABLE `anuario_tipoinversion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipomovimiento`
--

CREATE TABLE `anuario_tipomovimiento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_valorcuota`
--

CREATE TABLE `anuario_valorcuota` (
  `bindex_id` int(11) NOT NULL,
  `anio` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `datos` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `anuario_asignacionactivo`
--
ALTER TABLE `anuario_asignacionactivo`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `anuario_bindex`
--
ALTER TABLE `anuario_bindex`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_branding`
--
ALTER TABLE `anuario_branding`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_broadcategory`
--
ALTER TABLE `anuario_broadcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_carteracliente`
--
ALTER TABLE `anuario_carteracliente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_carteracliente_bindex_id_8895a68e_fk_anuario_bindex_id` (`bindex_id`),
  ADD KEY `anuario_carteracliente_cliente_id_612d39cf_fk_anuario_cliente_id` (`cliente_id`),
  ADD KEY `anuario_carteraclien_tipoInversion_id_0d4a7a5f_fk_anuario_t` (`tipoInversion_id`);

--
-- Indices de la tabla `anuario_categoria`
--
ALTER TABLE `anuario_categoria`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_categoria_broadCategory_id_e748180a_fk_anuario_b` (`broadCategory_id`),
  ADD KEY `anuario_categoria_moneda_id_aac5227f_fk_anuario_moneda_id` (`moneda_id`);

--
-- Indices de la tabla `anuario_claseactivo`
--
ALTER TABLE `anuario_claseactivo`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `anuario_cliente`
--
ALTER TABLE `anuario_cliente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_countryexposure`
--
ALTER TABLE `anuario_countryexposure`
  ADD PRIMARY KEY (`bindex_id`),
  ADD UNIQUE KEY `anuario_countryexposure_bindex_id_f44c72a8_uniq` (`bindex_id`);

--
-- Indices de la tabla `anuario_domicilio`
--
ALTER TABLE `anuario_domicilio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_fondo`
--
ALTER TABLE `anuario_fondo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_fondo_categoria_id_ca151073_fk_anuario_categoria_id` (`categoria_id`),
  ADD KEY `anuario_fondo_domicilio_id_520d51df_fk_anuario_domicilio_id` (`domicilio_id`),
  ADD KEY `anuario_fondo_moneda_id_0b19afe0_fk_anuario_moneda_id` (`moneda_id`);

--
-- Indices de la tabla `anuario_frecuenciadistribucion`
--
ALTER TABLE `anuario_frecuenciadistribucion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_instrumento`
--
ALTER TABLE `anuario_instrumento`
  ADD PRIMARY KEY (`bindex_id`),
  ADD KEY `anuario_instrumento_branding_id_37449f90_fk_anuario_branding_id` (`branding_id`),
  ADD KEY `anuario_instrumento_fondo_id_686af8ba_fk_anuario_fondo_id` (`fondo_id`),
  ADD KEY `anuario_instrumento_frecuenciaDistribuci_0dd3872e_fk_anuario_f` (`frecuenciaDistribucion_id`),
  ADD KEY `anuario_instrumento_proveedor_id_25ed6ac6_fk_anuario_p` (`proveedor_id`),
  ADD KEY `anuario_instrumento_rendimiento_id_734f999d_fk_anuario_r` (`rendimiento_id`),
  ADD KEY `anuario_instrumento_tipoInstrumento_id_0507c0c9_fk_anuario_t` (`tipoInstrumento_id`);

--
-- Indices de la tabla `anuario_moneda`
--
ALTER TABLE `anuario_moneda`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_movimiento`
--
ALTER TABLE `anuario_movimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_movimiento_bindex_id_c55b48c6_fk_anuario_bindex_id` (`bindex_id`),
  ADD KEY `anuario_movimiento_cliente_id_f1f7c1af_fk_anuario_cliente_id` (`cliente_id`),
  ADD KEY `anuario_movimiento_tipoInversion_id_e8cf84d0_fk_anuario_t` (`tipoInversion_id`),
  ADD KEY `anuario_movimiento_tipoMovimiento_id_dd55e113_fk_anuario_t` (`tipoMovimiento_id`);

--
-- Indices de la tabla `anuario_pais`
--
ALTER TABLE `anuario_pais`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_precio_actual`
--
ALTER TABLE `anuario_precio_actual`
  ADD PRIMARY KEY (`bindex_id`),
  ADD KEY `anuario_precio_actua_CurrencyISO3_id_31d10a7b_fk_anuario_m` (`CurrencyISO3_id`);

--
-- Indices de la tabla `anuario_proveedor`
--
ALTER TABLE `anuario_proveedor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_rendimiento`
--
ALTER TABLE `anuario_rendimiento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_rentabilidad`
--
ALTER TABLE `anuario_rentabilidad`
  ADD PRIMARY KEY (`bindex_id`),
  ADD KEY `anuario_rentabilidad_fondo_id_554eb4e4_fk_anuario_fondo_id` (`fondo_id`);

--
-- Indices de la tabla `anuario_rentafija`
--
ALTER TABLE `anuario_rentafija`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `anuario_reporte_anual_couta`
--
ALTER TABLE `anuario_reporte_anual_couta`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `anuario_saldoactualizado`
--
ALTER TABLE `anuario_saldoactualizado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_saldoactualizado_bindex_id_bb408a8c_fk_anuario_bindex_id` (`bindex_id`),
  ADD KEY `anuario_saldoactuali_cliente_id_85b3174f_fk_anuario_c` (`cliente_id`),
  ADD KEY `anuario_saldoactuali_tipoInversion_id_53336641_fk_anuario_t` (`tipoInversion_id`);

--
-- Indices de la tabla `anuario_saldomensual`
--
ALTER TABLE `anuario_saldomensual`
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_saldomensual_cliente_id_cca09015_fk_anuario_cliente_id` (`cliente_id`),
  ADD KEY `anuario_saldomensual_tipoInversion_id_be62c960_fk_anuario_t` (`tipoInversion_id`);

--
-- Indices de la tabla `anuario_sector`
--
ALTER TABLE `anuario_sector`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `anuario_tipoinstrumento`
--
ALTER TABLE `anuario_tipoinstrumento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_tipoinversion`
--
ALTER TABLE `anuario_tipoinversion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_tipomovimiento`
--
ALTER TABLE `anuario_tipomovimiento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `anuario_valorcuota`
--
ALTER TABLE `anuario_valorcuota`
  ADD PRIMARY KEY (`bindex_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `anuario_bindex`
--
ALTER TABLE `anuario_bindex`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2492;

--
-- AUTO_INCREMENT de la tabla `anuario_carteracliente`
--
ALTER TABLE `anuario_carteracliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `anuario_cliente`
--
ALTER TABLE `anuario_cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `anuario_frecuenciadistribucion`
--
ALTER TABLE `anuario_frecuenciadistribucion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `anuario_movimiento`
--
ALTER TABLE `anuario_movimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=349;

--
-- AUTO_INCREMENT de la tabla `anuario_saldoactualizado`
--
ALTER TABLE `anuario_saldoactualizado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=262;

--
-- AUTO_INCREMENT de la tabla `anuario_saldomensual`
--
ALTER TABLE `anuario_saldomensual`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;

--
-- AUTO_INCREMENT de la tabla `anuario_tipoinversion`
--
ALTER TABLE `anuario_tipoinversion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `anuario_tipomovimiento`
--
ALTER TABLE `anuario_tipomovimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `anuario_asignacionactivo`
--
ALTER TABLE `anuario_asignacionactivo`
  ADD CONSTRAINT `anuario_asignacionactivo_bindex_id_f7bd5cae_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_carteracliente`
--
ALTER TABLE `anuario_carteracliente`
  ADD CONSTRAINT `anuario_carteraclien_tipoInversion_id_0d4a7a5f_fk_anuario_t` FOREIGN KEY (`tipoInversion_id`) REFERENCES `anuario_tipoinversion` (`id`),
  ADD CONSTRAINT `anuario_carteracliente_bindex_id_8895a68e_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`),
  ADD CONSTRAINT `anuario_carteracliente_cliente_id_612d39cf_fk_anuario_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `anuario_cliente` (`id`);

--
-- Filtros para la tabla `anuario_categoria`
--
ALTER TABLE `anuario_categoria`
  ADD CONSTRAINT `anuario_categoria_broadCategory_id_e748180a_fk_anuario_b` FOREIGN KEY (`broadCategory_id`) REFERENCES `anuario_broadcategory` (`id`),
  ADD CONSTRAINT `anuario_categoria_moneda_id_aac5227f_fk_anuario_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `anuario_moneda` (`id`);

--
-- Filtros para la tabla `anuario_claseactivo`
--
ALTER TABLE `anuario_claseactivo`
  ADD CONSTRAINT `anuario_claseactivo_bindex_id_ccb59e40_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_countryexposure`
--
ALTER TABLE `anuario_countryexposure`
  ADD CONSTRAINT `anuario_countryexposure_bindex_id_f44c72a8_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_fondo`
--
ALTER TABLE `anuario_fondo`
  ADD CONSTRAINT `anuario_fondo_categoria_id_ca151073_fk_anuario_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `anuario_categoria` (`id`),
  ADD CONSTRAINT `anuario_fondo_domicilio_id_520d51df_fk_anuario_domicilio_id` FOREIGN KEY (`domicilio_id`) REFERENCES `anuario_domicilio` (`id`),
  ADD CONSTRAINT `anuario_fondo_moneda_id_0b19afe0_fk_anuario_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `anuario_moneda` (`id`);

--
-- Filtros para la tabla `anuario_instrumento`
--
ALTER TABLE `anuario_instrumento`
  ADD CONSTRAINT `anuario_instrumento_bindex_id_ff5dc1d3_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`),
  ADD CONSTRAINT `anuario_instrumento_branding_id_37449f90_fk_anuario_branding_id` FOREIGN KEY (`branding_id`) REFERENCES `anuario_branding` (`id`),
  ADD CONSTRAINT `anuario_instrumento_fondo_id_686af8ba_fk_anuario_fondo_id` FOREIGN KEY (`fondo_id`) REFERENCES `anuario_fondo` (`id`),
  ADD CONSTRAINT `anuario_instrumento_frecuenciaDistribuci_0dd3872e_fk_anuario_f` FOREIGN KEY (`frecuenciaDistribucion_id`) REFERENCES `anuario_frecuenciadistribucion` (`id`),
  ADD CONSTRAINT `anuario_instrumento_proveedor_id_25ed6ac6_fk_anuario_p` FOREIGN KEY (`proveedor_id`) REFERENCES `anuario_proveedor` (`id`),
  ADD CONSTRAINT `anuario_instrumento_rendimiento_id_734f999d_fk_anuario_r` FOREIGN KEY (`rendimiento_id`) REFERENCES `anuario_rendimiento` (`id`),
  ADD CONSTRAINT `anuario_instrumento_tipoInstrumento_id_0507c0c9_fk_anuario_t` FOREIGN KEY (`tipoInstrumento_id`) REFERENCES `anuario_tipoinstrumento` (`id`);

--
-- Filtros para la tabla `anuario_movimiento`
--
ALTER TABLE `anuario_movimiento`
  ADD CONSTRAINT `anuario_movimiento_bindex_id_c55b48c6_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`),
  ADD CONSTRAINT `anuario_movimiento_cliente_id_f1f7c1af_fk_anuario_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `anuario_cliente` (`id`),
  ADD CONSTRAINT `anuario_movimiento_tipoInversion_id_e8cf84d0_fk_anuario_t` FOREIGN KEY (`tipoInversion_id`) REFERENCES `anuario_tipoinversion` (`id`),
  ADD CONSTRAINT `anuario_movimiento_tipoMovimiento_id_dd55e113_fk_anuario_t` FOREIGN KEY (`tipoMovimiento_id`) REFERENCES `anuario_tipomovimiento` (`id`);

--
-- Filtros para la tabla `anuario_precio_actual`
--
ALTER TABLE `anuario_precio_actual`
  ADD CONSTRAINT `anuario_precio_actua_CurrencyISO3_id_31d10a7b_fk_anuario_m` FOREIGN KEY (`CurrencyISO3_id`) REFERENCES `anuario_moneda` (`id`),
  ADD CONSTRAINT `anuario_precio_actual_bindex_id_60270c9b_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_rentabilidad`
--
ALTER TABLE `anuario_rentabilidad`
  ADD CONSTRAINT `anuario_rentabilidad_bindex_id_929b9504_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`),
  ADD CONSTRAINT `anuario_rentabilidad_fondo_id_554eb4e4_fk_anuario_fondo_id` FOREIGN KEY (`fondo_id`) REFERENCES `anuario_fondo` (`id`);

--
-- Filtros para la tabla `anuario_rentafija`
--
ALTER TABLE `anuario_rentafija`
  ADD CONSTRAINT `anuario_rentafija_bindex_id_4fa6dedb_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_reporte_anual_couta`
--
ALTER TABLE `anuario_reporte_anual_couta`
  ADD CONSTRAINT `anuario_reporte_anua_bindex_id_0a78c466_fk_anuario_b` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_saldoactualizado`
--
ALTER TABLE `anuario_saldoactualizado`
  ADD CONSTRAINT `anuario_saldoactuali_cliente_id_85b3174f_fk_anuario_c` FOREIGN KEY (`cliente_id`) REFERENCES `anuario_cliente` (`id`),
  ADD CONSTRAINT `anuario_saldoactuali_tipoInversion_id_53336641_fk_anuario_t` FOREIGN KEY (`tipoInversion_id`) REFERENCES `anuario_tipoinversion` (`id`),
  ADD CONSTRAINT `anuario_saldoactualizado_bindex_id_bb408a8c_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_saldomensual`
--
ALTER TABLE `anuario_saldomensual`
  ADD CONSTRAINT `anuario_saldomensual_cliente_id_cca09015_fk_anuario_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `anuario_cliente` (`id`),
  ADD CONSTRAINT `anuario_saldomensual_tipoInversion_id_be62c960_fk_anuario_t` FOREIGN KEY (`tipoInversion_id`) REFERENCES `anuario_tipoinversion` (`id`);

--
-- Filtros para la tabla `anuario_sector`
--
ALTER TABLE `anuario_sector`
  ADD CONSTRAINT `anuario_sector_bindex_id_079b0df3_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `anuario_valorcuota`
--
ALTER TABLE `anuario_valorcuota`
  ADD CONSTRAINT `anuario_valorcuota_bindex_id_33204bb9_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
