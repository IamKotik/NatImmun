from rest_framework import serializers

from core.models import Vaccinations, VaccinationsEpid, VaccinationsNat, VaccinatedPersonsNat


class VaccinationsEpidSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationsEpid
        fields = ['description']


class VaccinationsNatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationsNat
        fields = ['first_vac', 'second_vac', 'third_vac', 'third_risk', 'fourth_risk', 'first_revac', 'second_revac',
                  'third_revac', 'vaccination', 'revaccination']


class VaccinatedPersonsNatSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinatedPersonsNat
        fields = ['code', 'type', 'age', 'age_description', 'at_risk', 'risk_description']


class VaccinationsSerializer(serializers.ModelSerializer):
    vaccinations_epid = VaccinationsEpidSerializer(many=True, read_only=True)
    vaccinations_nat = VaccinationsNatSerializer(many=True, read_only=True)
    # vac_first_vaccin_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_first_vaccin_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_first_vaccin_three = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_second_vaccin_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_second_vaccin_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_second_vaccin_three = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_second_vaccin_four = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_vaccin_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_vaccin_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_vaccin_three = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_vaccin_four = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_vaccin_risk = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_fourth_vaccin_risk = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_first_revac_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_first_revac_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_second_revac = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_third_revac = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_vaccintaion_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_vaccintaion_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_vaccintaion_three = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_revaccintaion_one = VaccinatedPersonsNatSerializer(many=True, read_only=True)
    # vac_revaccintaion_two = VaccinatedPersonsNatSerializer(many=True, read_only=True)

    class Meta:
        model = Vaccinations
        fields = ['code', 'name', 'vaccinations_epid', 'vaccinations_nat']
        # fields = ['code', 'name', 'vaccinations_epid', 'vaccinations_nat', 'vac_first_vaccin_one',
        #           'vac_first_vaccin_two', 'vac_first_vaccin_three', 'vac_second_vaccin_one', 'vac_second_vaccin_two',
        #           'vac_second_vaccin_three', 'vac_second_vaccin_four', 'vac_third_vaccin_one', 'vac_third_vaccin_two',
        #           'vac_third_vaccin_three', 'vac_third_vaccin_four', 'vac_third_vaccin_risk', 'vac_fourth_vaccin_risk',
        #           'vac_first_revac_one', 'vac_first_revac_two', 'vac_second_revac', 'vac_third_revac',
        #           'vac_vaccintaion_one', 'vac_vaccintaion_two', 'vac_vaccintaion_three', 'vac_revaccintaion_one',
        #           'vac_revaccintaion_two']
