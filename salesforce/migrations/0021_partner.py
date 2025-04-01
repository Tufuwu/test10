# Generated by Django 2.2.5 on 2019-11-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0020_school_salesforce_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_type', models.CharField(max_length=255)),
                ('affordability_cost', models.CharField(max_length=255)),
                ('affordability_institutional', models.NullBooleanField()),
                ('app_available', models.NullBooleanField()),
                ('adaptivity_adaptive_presentation', models.NullBooleanField()),
                ('adaptivity_affective_state', models.NullBooleanField()),
                ('adaptivity_breadth_and_depth', models.NullBooleanField()),
                ('adaptivity_customized_path', models.NullBooleanField()),
                ('adaptivity_instructor_control', models.NullBooleanField()),
                ('adaptivity_quantitative_randomization', models.NullBooleanField()),
                ('adaptivity_varied_level', models.NullBooleanField()),
                ('admin_calendar_links', models.NullBooleanField()),
                ('admin_online_submission', models.NullBooleanField()),
                ('admin_realtime_progress', models.NullBooleanField()),
                ('admin_shared_students', models.NullBooleanField()),
                ('admin_syllabus', models.NullBooleanField()),
                ('assigment_outside_resources', models.NullBooleanField()),
                ('assignment_editing', models.NullBooleanField()),
                ('assignment_multimedia', models.NullBooleanField()),
                ('assignment_multiple_quantitative', models.NullBooleanField()),
                ('assignment_pretest', models.NullBooleanField()),
                ('address_Longitude', models.NullBooleanField()),
                ('assignment_scientific_structures', models.NullBooleanField()),
                ('assignment_summative_assessments', models.NullBooleanField()),
                ('autonomy_digital_badges', models.NullBooleanField()),
                ('autonomy_on_demand_extras', models.NullBooleanField()),
                ('autonomy_self_reflection', models.NullBooleanField()),
                ('collaboration_peer_feedback', models.NullBooleanField()),
                ('collaboration_peer_interaction', models.NullBooleanField()),
                ('collaboration_teacher_learner_contact', models.NullBooleanField()),
                ('collaboration_tutor', models.NullBooleanField()),
                ('content_batch_uploads', models.NullBooleanField()),
                ('content_resource_sharing', models.NullBooleanField()),
                ('content_sharing_among_courses', models.NullBooleanField()),
                ('customization_assessement_repository', models.NullBooleanField()),
                ('customization_create_learning_outcomes', models.NullBooleanField()),
                ('customization_reorder_content', models.NullBooleanField()),
                ('customization_reorder_learning_outcomes', models.NullBooleanField()),
                ('feedback_early_warning', models.NullBooleanField()),
                ('feedback_knowledge_gaps', models.NullBooleanField()),
                ('feedback_learner_progress_tasks', models.NullBooleanField()),
                ('feedback_multipart', models.NullBooleanField()),
                ('feedback_understanding', models.NullBooleanField()),
                ('grading_change_scores', models.NullBooleanField()),
                ('grading_class_and_student_level', models.NullBooleanField()),
                ('grading_group_work', models.NullBooleanField()),
                ('grading_learning_portfolio', models.NullBooleanField()),
                ('grading_rubric_based', models.NullBooleanField()),
                ('grading_tolerances_sig_fig', models.NullBooleanField()),
                ('interactivity_annotate', models.NullBooleanField()),
                ('interactivity_different_representations', models.NullBooleanField()),
                ('interactivity_gaming', models.NullBooleanField()),
                ('interactivity_previous_knowledge', models.NullBooleanField()),
                ('interactivity_simulations', models.NullBooleanField()),
                ('interactivity_varying_means', models.NullBooleanField()),
                ('LMS_analytics', models.NullBooleanField()),
                ('LMS_sends_grades', models.NullBooleanField()),
                ('LMS_SSO', models.NullBooleanField()),
                ('measure_alternate_assessment', models.NullBooleanField()),
                ('measure_assessments_in_most', models.NullBooleanField()),
                ('measure_mapping', models.NullBooleanField()),
                ('reporting_competency', models.NullBooleanField()),
                ('reporting_student_workload', models.NullBooleanField()),
                ('scaffolding_hints', models.NullBooleanField()),
                ('scaffolding_learner_explanations', models.NullBooleanField()),
                ('scaffolding_mental_practice', models.NullBooleanField()),
                ('scaffolding_narrative', models.NullBooleanField()),
                ('scaffolding_social_intervention', models.NullBooleanField()),
                ('usability_design_orients_users', models.NullBooleanField()),
                ('usability_glossary', models.NullBooleanField()),
                ('usability_partial_progress', models.NullBooleanField()),
                ('accessibility_language_UI', models.NullBooleanField()),
                ('accessibility_language_content', models.NullBooleanField()),
                ('accessibility_VPAT', models.NullBooleanField()),
                ('accessibility_WCAG', models.NullBooleanField()),
                ('accessibility_universal_design', models.NullBooleanField()),
            ],
        ),
    ]
