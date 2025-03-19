from behave import given, when, then
from astre.astre import Astre
from astre.planet import Planet
import math

@given('un astre nommé "{nom}" avec un diamètre de {diametre:d} km')
def step_impl(context, nom, diametre):
    context.astre = Astre(nom, diametre)

@given('une longueur moyenne de tête humaine de {tete:f} m')
def step_impl(context, tete):
    context.longueur_tete = tete / 1000  # Convert meters to kilometers

@when('je calcule la proportion entre le Soleil et la tête humaine')
def step_impl(context):
    context.proportion = context.astre.get_proportion(context.longueur_tete)


@then('la proportion devrait être environ {valeur:d} avec une marge de {delta:d}')
def step_impl(context, valeur, delta):
    assert abs(context.proportion - valeur) <= delta

@given('une planète nommée "{nom}" avec diamètre de {diametre:d} km')
def step_impl(context, nom, diametre):
    if not hasattr(context, 'planetes'):
        context.planetes = {}
    context.planetes[nom] = Planet(nom, diametre)

@when('je mets à l\'échelle les diamètres de ces planètes selon la proportion Soleil-tête')
def step_impl(context):
    # context.proportion = context.astre.get_proportion(0.22 / 1000)  # 0.22m 转换为 km
    # context.scaled_planetes = {nom: planet.scale_down(context.proportion) for nom, planet in context.planetes.items()}

    if not hasattr(context, 'proportion'):
        context.proportion = context.astre.get_proportion(context.longueur_tete)
    context.scaled_planetes = {}
    for nom, planet in context.planetes.items():
        context.scaled_planetes[nom] = planet.scale_down(context.proportion)  # Convert km to mm

@then('le diamètre mis à l\'échelle de {nom} devrait être environ {diametre_scale:f} mm à {marge:f} mm près')
def step_impl(context, nom, diametre_scale, marge):
    scaled_diameter = context.scaled_planetes[nom]
    diametre_scale = float(diametre_scale) 
    marge = float(marge)  

    assert math.isclose(scaled_diameter, diametre_scale, abs_tol=marge)
