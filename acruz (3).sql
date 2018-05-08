-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 08-05-2018 a las 14:30:34
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
  `red_bono` double NOT NULL,
  `red_efectivo` double NOT NULL,
  `red_convertible` double NOT NULL,
  `red_preferida` double NOT NULL,
  `red_acciones` double NOT NULL,
  `red_otra` double NOT NULL,
  `portafolio_fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_bindex`
--

CREATE TABLE `anuario_bindex` (
  `id` int(11) NOT NULL,
  `country_exposure` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_bindex`
--

INSERT INTO `anuario_bindex` (`id`, `country_exposure`) VALUES
(1, 'bindex1'),
(2, 'bindex2'),
(3, 'bindex3'),
(4, 'bindex4'),
(5, 'bindex5'),
(6, 'bindex6'),
(7, 'bindex7'),
(8, 'bindex8'),
(9, 'bindex9'),
(10, 'bindex10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_branding`
--

CREATE TABLE `anuario_branding` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_branding`
--

INSERT INTO `anuario_branding` (`id`, `nombre`) VALUES
('1', 'branding1'),
('2', 'branding2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_broadcategory`
--

CREATE TABLE `anuario_broadcategory` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_broadcategory`
--

INSERT INTO `anuario_broadcategory` (`id`, `nombre`) VALUES
('1', 'broadcategory1'),
('2', 'broadcategory2');

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
  `codigo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `broadCategory_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `moneda_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_categoria`
--

INSERT INTO `anuario_categoria` (`id`, `nombre`, `codigo`, `broadCategory_id`, `moneda_id`) VALUES
('1', 'categoria1', 'categoria1', '1', '1'),
('2', 'categoria2', 'categoria2', '2', '2');

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
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `tipoInversion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_cliente`
--

INSERT INTO `anuario_cliente` (`id`, `nombre`, `tipoInversion_id`) VALUES
(0, 'Seleccione', 1),
(1, 'cliente1', 1),
(2, 'cliente2', 2),
(3, 'cliente3', 1),
(4, 'cliente4', 1),
(5, 'cliente5', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_domicilio`
--

CREATE TABLE `anuario_domicilio` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_domicilio`
--

INSERT INTO `anuario_domicilio` (`id`, `nombre`) VALUES
('1', 'chile'),
('2', 'brasil');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_fondo`
--

CREATE TABLE `anuario_fondo` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_legal` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_inicio` date NOT NULL,
  `categoria_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `domicilio_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `moneda_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_fondo`
--

INSERT INTO `anuario_fondo` (`id`, `nombre`, `nombre_legal`, `fecha_inicio`, `categoria_id`, `domicilio_id`, `moneda_id`) VALUES
('1', 'Banchile Retorno L.P. UF E', 'Banchile Retorno L.P. UF E', '2018-05-16', '2', '2', '1'),
('10', 'BCI Gran Valor APV', 'BCI Gran Valor APV', '2018-05-09', '2', '1', '2'),
('2', 'Security Deuda Corp Latam IG H', 'Security Deuda Corp Latam IG H', '2018-05-01', '1', '1', '2'),
('3', 'BICE Acciones Mundo Activo D', 'BICE Acciones Mundo Activo D', '2018-05-02', '1', '2', '1'),
('4', 'BBVA Bonos Latam INSTI', 'BBVA Bonos Latam INSTI', '2018-05-01', '2', '2', '1'),
('5', 'Banchile Estratégia Agresiva C', 'Banchile Estratégia Agresiva C', '2018-05-17', '2', '1', '1'),
('6', 'Itaú Corporate C', 'Itaú Corporate C', '2018-05-10', '2', '2', '1'),
('7', 'BCI Selección Bursátil CLASI', 'BCI Selección Bursátil CLASI', '2018-05-09', '1', '2', '1'),
('8', 'BCI Rendimiento APV', 'BCI Rendimiento APV', '2018-05-01', '2', '1', '2'),
('9', 'BCI Rendimiento CLASI', 'BCI Rendimiento CLASI', '2018-05-10', '1', '2', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_frecuenciadistribucion`
--

CREATE TABLE `anuario_frecuenciadistribucion` (
  `id` int(11) NOT NULL,
  `frecuencia` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_frecuenciadistribucion`
--

INSERT INTO `anuario_frecuenciadistribucion` (`id`, `frecuencia`) VALUES
(1, 'frecuencia1'),
(2, 'frecuencia2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_instrumento`
--

CREATE TABLE `anuario_instrumento` (
  `bindex_id` int(11) NOT NULL,
  `run_svs` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `clase_proveedor` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `operation_ready` int(11) NOT NULL,
  `branding_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `fondo_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `frecuenciaDistribucion_id` int(11) NOT NULL,
  `proveedor_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `rendimiento_id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `tipoInstrumento_id` varchar(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_instrumento`
--

INSERT INTO `anuario_instrumento` (`bindex_id`, `run_svs`, `clase_proveedor`, `operation_ready`, `branding_id`, `fondo_id`, `frecuenciaDistribucion_id`, `proveedor_id`, `rendimiento_id`, `tipoInstrumento_id`) VALUES
(1, '1234', '123', 123, '2', '10', 2, '6', '2', '1'),
(2, '12345', '123', 123, '2', '9', 1, '6', '1', '1'),
(3, '1234', '123', 1234, '1', '8', 1, '6', '2', '1'),
(4, '123123', '1234', 123, '1', '7', 1, '6', '2', '1'),
(5, '1234', '123', 123, '1', '6', 1, '5', '1', '1'),
(6, '1234', '1234', 1234, '1', '5', 1, '1', '1', '1'),
(7, '123', '123', 123, '2', '4', 1, '4', '1', '2'),
(8, '123', '123', 123, '1', '3', 1, '3', '1', '2'),
(9, '123', '123', 123, '2', '2', 2, '2', '1', '2'),
(10, '123', '123', 123, '1', '1', 1, '1', '1', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_moneda`
--

CREATE TABLE `anuario_moneda` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_moneda`
--

INSERT INTO `anuario_moneda` (`id`, `nombre`) VALUES
('1', 'pesos'),
('2', 'real');

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

--
-- Volcado de datos para la tabla `anuario_movimiento`
--

INSERT INTO `anuario_movimiento` (`id`, `monto`, `fecha`, `numero_cuotas`, `bindex_id`, `cliente_id`, `tipoInversion_id`, `tipoMovimiento_id`) VALUES
(1, 123, '2018-10-05', 0, 6, 3, 2, 1),
(2, 212123, '2018-05-14', 0, 6, 2, 2, 1),
(3, 2345, '2018-05-10', 0, 6, 2, 3, 3),
(4, 1234566, '2018-05-10', 0, 5, 2, 1, 1),
(5, 200000, '2018-05-17', 0, 4, 2, 1, 2),
(6, 432, '2018-05-08', 0, 3, 3, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_pais`
--

CREATE TABLE `anuario_pais` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_proveedor`
--

CREATE TABLE `anuario_proveedor` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `datos` longtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_proveedor`
--

INSERT INTO `anuario_proveedor` (`id`, `datos`) VALUES
('1', 'Banchile AGF S.A.'),
('2', 'AGF Security S.A.'),
('3', 'Bice Inversiones AGF S.A.'),
('4', 'BBVA Asset Management AGF S.A.'),
('5', 'Itaú Chile AGF S.A.'),
('6', 'BCI Asset Management AGF S.A.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_rendimiento`
--

CREATE TABLE `anuario_rendimiento` (
  `id` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_rendimiento`
--

INSERT INTO `anuario_rendimiento` (`id`, `estado`) VALUES
('1', 1),
('2', 2);

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
-- Estructura de tabla para la tabla `anuario_sector`
--

CREATE TABLE `anuario_sector` (
  `bindex_id` int(11) NOT NULL,
  `materiales_basicos` double NOT NULL,
  `servicio_comunicacion` double NOT NULL,
  `ciclico_consumidor` double NOT NULL,
  `defensa_consumidor` double NOT NULL,
  `energia` double NOT NULL,
  `servicios_financieros` double NOT NULL,
  `cuidado_salud` double NOT NULL,
  `acciones_industriales` double NOT NULL,
  `bienes_raices` double NOT NULL,
  `tecnologia` double NOT NULL,
  `utilidades` double NOT NULL,
  `portafolio_fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipoinstrumento`
--

CREATE TABLE `anuario_tipoinstrumento` (
  `id` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `estructura_legal` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `estado_distribucion` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_tipoinstrumento`
--

INSERT INTO `anuario_tipoinstrumento` (`id`, `estructura_legal`, `estado_distribucion`) VALUES
('', '', 'Seleccione'),
('1', 'Open Ended Investment Company', 'Accumulated'),
('2', 'Open Ended Investment Company', 'Income');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipoinversion`
--

CREATE TABLE `anuario_tipoinversion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_tipoinversion`
--

INSERT INTO `anuario_tipoinversion` (`id`, `nombre`) VALUES
(0, 'Seleccione'),
(1, 'APV'),
(2, 'FFMM'),
(3, 'ETC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `anuario_tipomovimiento`
--

CREATE TABLE `anuario_tipomovimiento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `anuario_tipomovimiento`
--

INSERT INTO `anuario_tipomovimiento` (`id`, `nombre`) VALUES
(1, 'Saldo inicial'),
(2, 'Aporte'),
(3, 'Retiro');

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

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add cartera cliente', 1, 'add_carteracliente'),
(2, 'Can change cartera cliente', 1, 'change_carteracliente'),
(3, 'Can delete cartera cliente', 1, 'delete_carteracliente'),
(4, 'Can add frecuencia distribucion', 2, 'add_frecuenciadistribucion'),
(5, 'Can change frecuencia distribucion', 2, 'change_frecuenciadistribucion'),
(6, 'Can delete frecuencia distribucion', 2, 'delete_frecuenciadistribucion'),
(7, 'Can add tipo inversion', 3, 'add_tipoinversion'),
(8, 'Can change tipo inversion', 3, 'change_tipoinversion'),
(9, 'Can delete tipo inversion', 3, 'delete_tipoinversion'),
(10, 'Can add tipo movimiento', 4, 'add_tipomovimiento'),
(11, 'Can change tipo movimiento', 4, 'change_tipomovimiento'),
(12, 'Can delete tipo movimiento', 4, 'delete_tipomovimiento'),
(13, 'Can add movimiento', 5, 'add_movimiento'),
(14, 'Can change movimiento', 5, 'change_movimiento'),
(15, 'Can delete movimiento', 5, 'delete_movimiento'),
(16, 'Can add proveedor', 6, 'add_proveedor'),
(17, 'Can change proveedor', 6, 'change_proveedor'),
(18, 'Can delete proveedor', 6, 'delete_proveedor'),
(19, 'Can add pais', 7, 'add_pais'),
(20, 'Can change pais', 7, 'change_pais'),
(21, 'Can delete pais', 7, 'delete_pais'),
(22, 'Can add branding', 8, 'add_branding'),
(23, 'Can change branding', 8, 'change_branding'),
(24, 'Can delete branding', 8, 'delete_branding'),
(25, 'Can add valor cuota', 9, 'add_valorcuota'),
(26, 'Can change valor cuota', 9, 'change_valorcuota'),
(27, 'Can delete valor cuota', 9, 'delete_valorcuota'),
(28, 'Can add cliente', 10, 'add_cliente'),
(29, 'Can change cliente', 10, 'change_cliente'),
(30, 'Can delete cliente', 10, 'delete_cliente'),
(31, 'Can add sector', 11, 'add_sector'),
(32, 'Can change sector', 11, 'change_sector'),
(33, 'Can delete sector', 11, 'delete_sector'),
(34, 'Can add tipo instrumento', 12, 'add_tipoinstrumento'),
(35, 'Can change tipo instrumento', 12, 'change_tipoinstrumento'),
(36, 'Can delete tipo instrumento', 12, 'delete_tipoinstrumento'),
(37, 'Can add clase activo', 13, 'add_claseactivo'),
(38, 'Can change clase activo', 13, 'change_claseactivo'),
(39, 'Can delete clase activo', 13, 'delete_claseactivo'),
(40, 'Can add moneda', 14, 'add_moneda'),
(41, 'Can change moneda', 14, 'change_moneda'),
(42, 'Can delete moneda', 14, 'delete_moneda'),
(43, 'Can add renta fija', 15, 'add_rentafija'),
(44, 'Can change renta fija', 15, 'change_rentafija'),
(45, 'Can delete renta fija', 15, 'delete_rentafija'),
(46, 'Can add asignacion activo', 16, 'add_asignacionactivo'),
(47, 'Can change asignacion activo', 16, 'change_asignacionactivo'),
(48, 'Can delete asignacion activo', 16, 'delete_asignacionactivo'),
(49, 'Can add bindex', 17, 'add_bindex'),
(50, 'Can change bindex', 17, 'change_bindex'),
(51, 'Can delete bindex', 17, 'delete_bindex'),
(52, 'Can add instrumento', 18, 'add_instrumento'),
(53, 'Can change instrumento', 18, 'change_instrumento'),
(54, 'Can delete instrumento', 18, 'delete_instrumento'),
(55, 'Can add broad category', 19, 'add_broadcategory'),
(56, 'Can change broad category', 19, 'change_broadcategory'),
(57, 'Can delete broad category', 19, 'delete_broadcategory'),
(58, 'Can add categoria', 20, 'add_categoria'),
(59, 'Can change categoria', 20, 'change_categoria'),
(60, 'Can delete categoria', 20, 'delete_categoria'),
(61, 'Can add domicilio', 21, 'add_domicilio'),
(62, 'Can change domicilio', 21, 'change_domicilio'),
(63, 'Can delete domicilio', 21, 'delete_domicilio'),
(64, 'Can add rendimiento', 22, 'add_rendimiento'),
(65, 'Can change rendimiento', 22, 'change_rendimiento'),
(66, 'Can delete rendimiento', 22, 'delete_rendimiento'),
(67, 'Can add fondo', 23, 'add_fondo'),
(68, 'Can change fondo', 23, 'change_fondo'),
(69, 'Can delete fondo', 23, 'delete_fondo'),
(70, 'Can add log entry', 24, 'add_logentry'),
(71, 'Can change log entry', 24, 'change_logentry'),
(72, 'Can delete log entry', 24, 'delete_logentry'),
(73, 'Can add permission', 25, 'add_permission'),
(74, 'Can change permission', 25, 'change_permission'),
(75, 'Can delete permission', 25, 'delete_permission'),
(76, 'Can add user', 26, 'add_user'),
(77, 'Can change user', 26, 'change_user'),
(78, 'Can delete user', 26, 'delete_user'),
(79, 'Can add group', 27, 'add_group'),
(80, 'Can change group', 27, 'change_group'),
(81, 'Can delete group', 27, 'delete_group'),
(82, 'Can add content type', 28, 'add_contenttype'),
(83, 'Can change content type', 28, 'change_contenttype'),
(84, 'Can delete content type', 28, 'delete_contenttype'),
(85, 'Can add session', 29, 'add_session'),
(86, 'Can change session', 29, 'change_session'),
(87, 'Can delete session', 29, 'delete_session');

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

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$LMkp1bMhHoUM$WYOIKXZ0mNXt9GVO+Eev2nx/CAF1xN4c4wWxLMWZ1HQ=', '2018-05-07 12:37:23.784917', 1, 'benjaminsc', '', '', 'benjamin.salazar17@gmail.com', 1, 1, '2018-05-06 22:56:36.825437');

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

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(24, 'admin', 'logentry'),
(16, 'anuario', 'asignacionactivo'),
(17, 'anuario', 'bindex'),
(8, 'anuario', 'branding'),
(19, 'anuario', 'broadcategory'),
(1, 'anuario', 'carteracliente'),
(20, 'anuario', 'categoria'),
(13, 'anuario', 'claseactivo'),
(10, 'anuario', 'cliente'),
(21, 'anuario', 'domicilio'),
(23, 'anuario', 'fondo'),
(2, 'anuario', 'frecuenciadistribucion'),
(18, 'anuario', 'instrumento'),
(14, 'anuario', 'moneda'),
(5, 'anuario', 'movimiento'),
(7, 'anuario', 'pais'),
(6, 'anuario', 'proveedor'),
(22, 'anuario', 'rendimiento'),
(15, 'anuario', 'rentafija'),
(11, 'anuario', 'sector'),
(12, 'anuario', 'tipoinstrumento'),
(3, 'anuario', 'tipoinversion'),
(4, 'anuario', 'tipomovimiento'),
(9, 'anuario', 'valorcuota'),
(27, 'auth', 'group'),
(25, 'auth', 'permission'),
(26, 'auth', 'user'),
(28, 'contenttypes', 'contenttype'),
(29, 'sessions', 'session');

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

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-05-06 20:53:48.431823'),
(2, 'auth', '0001_initial', '2018-05-06 20:53:59.683503'),
(3, 'admin', '0001_initial', '2018-05-06 20:54:02.193432'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-05-06 20:54:02.266325'),
(5, 'anuario', '0001_initial', '2018-05-06 20:54:50.917741'),
(6, 'contenttypes', '0002_remove_content_type_name', '2018-05-06 20:54:52.602819'),
(7, 'auth', '0002_alter_permission_name_max_length', '2018-05-06 20:54:53.997183'),
(8, 'auth', '0003_alter_user_email_max_length', '2018-05-06 20:54:55.136874'),
(9, 'auth', '0004_alter_user_username_opts', '2018-05-06 20:54:55.210878'),
(10, 'auth', '0005_alter_user_last_login_null', '2018-05-06 20:54:56.684140'),
(11, 'auth', '0006_require_contenttypes_0002', '2018-05-06 20:54:56.750823'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2018-05-06 20:54:56.804373'),
(13, 'auth', '0008_alter_user_username_max_length', '2018-05-06 20:54:59.474752'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2018-05-06 20:55:00.477518'),
(15, 'sessions', '0001_initial', '2018-05-06 20:55:01.184518');

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
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9jef7izlgs5jkl56cyv84qvzmevwujo2', 'MDJhM2ZjZmUxZjNhMDMyYTlhZDNkOWUyMDdmZjRlMWVlYzc3ZTVhMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YTQ3YjBkNTVmYjY1MTg2MzFmMTFiM2U4MGJkOWQ4NDhhN2I1NjQ4In0=', '2018-05-21 12:37:23.842931'),
('pxzho429fm8ez3ztyzkeyz99def495iz', 'MDJhM2ZjZmUxZjNhMDMyYTlhZDNkOWUyMDdmZjRlMWVlYzc3ZTVhMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3YTQ3YjBkNTVmYjY1MTg2MzFmMTFiM2U4MGJkOWQ4NDhhN2I1NjQ4In0=', '2018-05-20 22:57:46.740039');

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
  ADD PRIMARY KEY (`id`),
  ADD KEY `anuario_cliente_tipoInversion_id_7899199a_fk_anuario_t` (`tipoInversion_id`);

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
-- Indices de la tabla `anuario_rentafija`
--
ALTER TABLE `anuario_rentafija`
  ADD PRIMARY KEY (`bindex_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `anuario_carteracliente`
--
ALTER TABLE `anuario_carteracliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `anuario_cliente`
--
ALTER TABLE `anuario_cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `anuario_frecuenciadistribucion`
--
ALTER TABLE `anuario_frecuenciadistribucion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `anuario_movimiento`
--
ALTER TABLE `anuario_movimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `anuario_tipoinversion`
--
ALTER TABLE `anuario_tipoinversion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

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
-- Filtros para la tabla `anuario_cliente`
--
ALTER TABLE `anuario_cliente`
  ADD CONSTRAINT `anuario_cliente_tipoInversion_id_7899199a_fk_anuario_t` FOREIGN KEY (`tipoInversion_id`) REFERENCES `anuario_tipoinversion` (`id`);

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
-- Filtros para la tabla `anuario_rentafija`
--
ALTER TABLE `anuario_rentafija`
  ADD CONSTRAINT `anuario_rentafija_bindex_id_4fa6dedb_fk_anuario_bindex_id` FOREIGN KEY (`bindex_id`) REFERENCES `anuario_bindex` (`id`);

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
