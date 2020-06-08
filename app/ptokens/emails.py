'''
    Copyright (C) 2019 Gitcoin Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.translation import gettext as _

from dashboard.models import Profile
from retail.emails import premailer_transform


def render_personal_token_created(network, symbol, name, address):
    params = {'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_created.html", params))
    response_txt = render_to_string("emails/personal_token_created.txt", params)
    subject = _("Your personal token created")
    return response_html, response_txt, subject


def render_personal_token_redeem_requested(to_profile, network, symbol, name, address):
    params = {'to_profile': to_profile, 'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_redeem_requested.html", params))
    response_txt = render_to_string("emails/personal_token_redeem_requested.txt", params)
    subject = _("Personal token redeem requested")
    return response_html, response_txt, subject


def render_personal_token_redeem_accepted(from_profile, network, symbol, name, address):
    params = {'from_profile': from_profile, 'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_redeem_accepted.html", params))
    response_txt = render_to_string("emails/personal_token_redeem_accepted.txt", params)
    subject = _("Personal token redeem accepted")
    return response_html, response_txt, subject


def render_personal_token_redeem_rejected(from_profile, network, symbol, name, address):
    params = {'from_profile': from_profile, 'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_redeem_rejected.html", params))
    response_txt = render_to_string("emails/personal_token_redeem_rejected.txt", params)
    subject = _("Personal token redeem rejected")
    return response_html, response_txt, subject


def render_personal_token_redeem_complete_sender(to_profile, network, symbol, name, address):
    params = {'to_profile': to_profile, 'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_redeem_complete_sender.html", params))
    response_txt = render_to_string("emails/personal_token_redeem_complete_sender.txt", params)
    subject = _("Your personal token redeem complete")
    return response_html, response_txt, subject


def render_personal_token_redeem_complete_receiver(from_profile, network, symbol, name, address):
    params = {'from_profile': from_profile, 'network': network, 'symbol': symbol, 'name': name, 'address': address}
    response_html = premailer_transform(render_to_string("emails/personal_token_redeem_complete_receiver.html", params))
    response_txt = render_to_string("emails/personal_token_redeem_complete_receiver.txt", params)
    subject = _("Redeem of personal token to you complete")
    return response_html, response_txt, subject


@staff_member_required
def personal_token_created():
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    response_html, _, _ = render_personal_token_created('mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)


@staff_member_required
def personal_token_redeem_requested(request, profile_id):
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    profile = Profile.objects.get(pk=profile_id)
    response_html, _, _ = render_personal_token_redeem_requested(profile, 'mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)


@staff_member_required
def personal_token_redeem_accepted(request, profile_id):
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    profile = Profile.objects.get(pk=profile_id)
    response_html, _, _ = render_personal_token_redeem_accepted(profile, 'mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)


@staff_member_required
def personal_token_redeem_rejected(request, profile_id):
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    profile = Profile.objects.get(pk=profile_id)
    response_html, _, _ = render_personal_token_redeem_rejected(profile, 'mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)


@staff_member_required
def personal_token_redeem_complete_sender(request, profile_id):
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    profile = Profile.objects.get(pk=profile_id)
    response_html, _, _ = render_personal_token_redeem_complete_sender(profile, 'mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)


@staff_member_required
def personal_token_redeem_complete_receiver(request, profile_id):
    address = '0x2460e7Da41D5c5B1e41D645E3bF63fC6f9E7A323'  # completely random
    profile = Profile.objects.get(pk=profile_id)
    response_html, _, _ = render_personal_token_redeem_complete_sender(profile, 'mainnet', 'TST', 'Test Token', address)
    return HttpResponse(response_html)
