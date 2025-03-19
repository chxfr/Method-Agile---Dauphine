from behave import given, when, then
from astre.astre import Astre
from astre.planet import Planet

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
    if not hasattr(context, 'proportion'):
        context.proportion = context.astre.get_proportion(context.longueur_tete)
    context.diametre_scale = {}
    for nom_p, planet in context.planetes.items():
        context.diametre_scale[nom_p] = planet.scale_down(context.proportion)  # Convert km to mm

@then('le diamètre mis à l\'échelle de {nom_p} devrait être environ {diametre_scale:f} mm à 0.1 mm près')
def step_impl(context, nom_p, diametre_scale):
    diametre_obtenu = context.diametre_scale[nom_p]
    context.diametre_scale_attendu = diametre_scale