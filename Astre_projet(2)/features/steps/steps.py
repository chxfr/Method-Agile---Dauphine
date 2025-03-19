from behave import given, when, then
from astre.astre import Astre
from astre.planet import Planet
from astre.distance import Distance
import math



# 存储行星对象
@given('un astre nommé "{nom}" avec un diamètre de {diametre:d} km')
def step_given_astre(context, nom, diametre):
    """创建一个 Astre（天体）对象"""
    context.astre = Astre(nom, diametre)

@given('une planète nommée "{nom}" avec un diamètre de {diametre} km')
def step_given_planete(context, nom, diametre):
    if not hasattr(context, "planetes"):
        context.planetes = {}
    context.planetes[nom] = Planet(nom, diametre)
    print(f"✅ Ajout de la planète: {nom}, diamètre: {diametre} km") 

@when("je mets les planètes à l'échelle d'une tête humaine")
def step_when_scale_planetes(context):
    """计算缩放比例，并缩小所有行星的直径"""
    context.proportion = context.astre.get_proportion(0.22 / 1000)  # 0.22m 转换为 km
    context.scaled_planetes = {nom: planet.scale_down(context.proportion) for nom, planet in context.planetes.items()}

@then('le diamètre de "{nom}" devrait être environ {expected} mm avec une marge de {marge} mm')
def step_then_verifier_diametre(context, nom, expected, marge):
    """检查缩放后直径是否在误差范围内"""
    #scaled_diameter = float(context.scaled_planetes[nom])  # ✅ `scale_down()` 已经是 `mm`，不需要再乘 1000
    scaled_diameter = context.scaled_planetes[nom]
    expected = float(expected)  # ✅ 确保是 `float`
    marge = float(marge)  # ✅ 确保是 `float`

    assert math.isclose(scaled_diameter, expected, abs_tol=marge), \
        f"Échec : attendu {expected} ± {marge}, obtenu {scaled_diameter}"


